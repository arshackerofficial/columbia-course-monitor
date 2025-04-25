#!/usr/bin/env python3

import requests


def fetch_course_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def generate_markdown_table(courses):
    lines = ["| Course ID | Course Name |", "|-----------|-------------|"]
    for course in courses:
        course_id = course.get("id", "N/A")
        dept = course.get("Department", "")
        number = course.get("Course", "")
        section = course.get("Section", "")
        course_name = f"{dept} {number} sec {section}"
        lines.append(f"| {course_id} | {course_name} |")
    return "\n".join(lines)


def main():
    # Replace with your actual URL
    url = "https://student.columbiacollege.bc.ca/CourseOfferingJSON/Default.aspx?term=136&listType=offering"
    courses = fetch_course_data(url)
    markdown_table = generate_markdown_table(courses)
    with open("courses.md", "w") as f:
        f.write(markdown_table)
    print("Markdown table written to courses.md")


if __name__ == "__main__":
    main()
