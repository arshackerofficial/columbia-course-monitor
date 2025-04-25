import requests
import time
import tkinter as tk
import threading
import winsound
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# URL to monitor
URL = "https://student.columbiacollege.bc.ca/CourseOfferingJSON/Default.aspx?term=136&listType=offering"

# Target course IDs
# Find these ID's in Readme section of Github repo
target_ids = {"22239", "22353"}


# Function to play sound


def play_alert_sound():
    try:
        winsound.Beep(1000, 1000)  # 1000 Hz for 1 second
    except Exception as e:
        print("Sound error:", e)

# Function to show fullscreen alert


def show_fullscreen_alert(course_info):
    def close_alert(event=None):
        root.destroy()

    root = tk.Tk()
    root.title("COURSE ALERT")
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    label = tk.Label(
        root,
        text=f"Seats Now Available!\n\n{course_info}",
        fg="red",
        bg="black",
        font=("Helvetica", 36),
        justify="center"
    )
    label.pack(expand=True)

    root.bind("<Escape>", close_alert)
    root.after(15000, close_alert)  # auto close after 15 seconds
    root.mainloop()


def send_pushbullet_notification(title, body):
    try:
        API_KEY = "PUSHBULLET_API_KEY"
        data = {
            "type": "note",
            "title": title,
            "body": body
        }
        headers = {
            "Access-Token": API_KEY,
            "Content-Type": "application/json"
        }
        response = requests.post(
            "https://api.pushbullet.com/v2/pushes", json=data, headers=headers)
        if response.status_code != 200:
            print("❌ Pushbullet error:", response.text)
    except Exception as e:
        print("❌ Pushbullet exception:", e)


# Monitoring loop


def monitor():
    print("Starting monitor...")
    while True:
        try:
            response = requests.get(URL, verify=False)
            response.raise_for_status()
            data = response.json().get("data", [])

            for course in data:
                course_id = course.get("id")
                seats = course.get("SeatsRemaining", 0)
                name = course.get("CourseName", "N/A")
                if course_id in target_ids:
                    print(f"  [{course_id}] {name} - Seats: {seats}")

                if course_id in target_ids and seats > 0:
                    send_pushbullet_notification(
                        "Course Seats Alert 🚨", f"{name} now has {seats} seats!")
                    info = f"{course['CourseName']} (ID: {course_id})\nSeats Remaining: {seats}"
                    print(">>> Alert:", info)
                    threading.Thread(target=play_alert_sound).start()
                    show_fullscreen_alert(info)

        except Exception as e:
            print("Error:", e)

        time.sleep(1)
        print("Checking for updates...")


if __name__ == "__main__":
    monitor()
