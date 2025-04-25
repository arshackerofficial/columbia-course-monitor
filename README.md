# 📡 Columbia College Course Seat Monitor

A Python-based script that checks course availability every few seconds and notifies you in **multiple ways** (sound, fullscreen alert, and **Pushbullet notification**) when seats open up for your selected courses.

> Ideal for students trying to register in **high-demand classes** before they fill up again.

---

## 🚀 Features

- ⏱️ Polls the Columbia College course data API every 5 seconds
- 📊 Logs all available courses and seat counts to the terminal
- 🛑 Alerts you with a **beep** and **fullscreen warning** when a tracked course becomes available
- 📱 Sends a **Pushbullet notification** to your phone (fully customizable with apps like **BuzzKill**)
- 🔐 SSL verification disabled for compatibility with the API (you can re-enable if needed)
- 🧠 Easily extendable to track new courses every semester

---

## 📦 Requirements

- Python 3.6+
- `requests`
- `tkinter` (included by default)
- `winsound` (Windows only — replaceable with `pygame` or `playsound` on other OS)
- Pushbullet account + API token

```bash
pip install requests
```

---

## 🔧 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/columbia-course-monitor.git
   cd columbia-course-monitor
   ```

2. Replace `YOUR_PUSHBULLET_ACCESS_TOKEN` in the script with your actual token.

3. Run the script:
   ```bash
   python monitor.py
   ```

4. ✅ Done! You'll be notified on-screen, with sound, and via Pushbullet when seats are available.

---

## 📋 Tracked Courses

> You'll maintain the following table below by semester (automatically or manually):

| Course ID | Course Name |
|-----------|-------------|
| 22068 | ACCT 251 sec 16 |
| 22069 | ACCT 254 sec 12 |
| 22070 | ANTH 110 sec 14 |
| 22071 | ANTH 110 sec 19 |
| 22073 | ANTH 130 sec 15 |
| 22074 | ANTH 212 sec 10 |
| 22354 | ANTH 240 sec 121 |
| 22368 | APSC 160 sec 16H |
| 22076 | ARTH 100 sec 10 |
| 22077 | ARTH 100 sec 11 |
| 22078 | ARTH 100 sec 12 |
| 22079 | ARTH 100 sec 13 |
| 22082 | ARTH 210 sec FLEX |
| 22084 | ARTH 220 sec 9 |
| 22085 | ARTH 230 sec FLEX |
| 22087 | ARTH 250 sec 15 |
| 22088 | ASIA 110 sec 10 |
| 22090 | ASIA 131 sec 121 |
| 22093 | ASIA 131 sec 9 |
| 22094 | ASIA 213 sec 141 |
| 22095 | ASIA 213 sec FLEX |
| 22096 | ASIA 250 sec 11 |
| 22097 | BIOC 201 sec 161 |
| 22098 | BIOL 100 sec 10H |
| 22099 | BIOL 100 sec 13H |
| 22100 | BIOL 100 sec 19H |
| 22101 | BIOL 100L sec 105 |
| 22102 | BIOL 100L sec 145 |
| 22103 | BIOL 100L sec 1814 |
| 22105 | BIOL 105 sec 9H |
| 22107 | BIOL 105L sec 94 |
| 22108 | BIOL 110 sec 9H |
| 22110 | BIOL 110L sec 0814 |
| 22111 | BIOL 110L sec 1014 |
| 22113 | BIOL 120 sec 16H |
| 22115 | BIOL 120L sec 1614 |
| 22120 | BIOL 200 sec 121 |
| 22121 | BIOL 205 sec 12 |
| 22122 | BIOL 234 sec 10 |
| 22124 | BUSN 250 sec 11S |
| 22125 | BUSN 272 sec 9S |
| 22127 | BUSN 291 sec 14H |
| 22128 | CHEM 100 sec 12 |
| 22130 | CHEM 100 sec 15 |
| 22129 | CHEM 100 sec 17 |
| 22131 | CHEM 100L sec 115 |
| 22132 | CHEM 100L sec 125 |
| 22133 | CHEM 100L sec 155 |
| 22134 | CHEM 100L sec 175 |
| 22135 | CHEM 100L sec 95 |
| 22139 | CHEM 121 sec 15 |
| 22138 | CHEM 121 sec 8 |
| 22142 | CHEM 121L sec 0814 |
| 22371 | CHEM 121L sec 154 |
| 22372 | CHEM 121L sec 174 |
| 22143 | CHEM 123 sec 14 |
| 22145 | CHEM 123L sec 144 |
| 22146 | CHEM 123L sec 164 |
| 22147 | CHEM 210 sec 16 |
| 22148 | CHEM 210L sec 1614 |
| 22150 | CHEM 220 sec 13 |
| 22151 | CHEM 220L sec 114 |
| 22157 | CMNS 110 sec 101 |
| 22158 | CMNS 110 sec 17 |
| 22161 | CMNS 110 sec 18 |
| 22159 | CMNS 110 sec 9 |
| 22163 | CMNS 130 sec 12 |
| 22164 | CMNS 130 sec 13 |
| 22166 | CMNS 130 sec 161 |
| 22168 | CMNS 205 sec 16 |
| 22169 | CMNS 210 sec 14 |
| 22171 | CMNS 220 sec 10 |
| 22172 | CMNS 221 sec 8 |
| 22173 | CMNS 223 sec 13 |
| 22363 | CMNS 226 sec 12 |
| 22174 | CMNS 230 sec FLEX |
| 22175 | CMNS 253 sec 15 |
| 22176 | CMNS 262 sec 121 |
| 22178 | CRIM 100 sec 13 |
| 22179 | CRIM 100 sec 14 |
| 22182 | CRIM 150 sec 15 |
| 22184 | CRIM 220 sec 10 |
| 22185 | CRIM 251 sec FLEX |
| 22360 | CRIM 252 sec FLEX |
| 22187 | CSCI 101 sec 11 |
| 22186 | CSCI 101 sec 14H |
| 22188 | CSCI 101 sec 8 |
| 22190 | CSCI 120 sec 19 |
| 22192 | CSCI 125 sec 12H |
| 22191 | CSCI 125 sec 17 |
| 22193 | CSCI 150 sec 15 |
| 22195 | CSCI 165 sec 13 |
| 22197 | CSCI 165 sec 18 |
| 22196 | CSCI 165 sec 19 |
| 22194 | CSCI 165 sec 9 |
| 22198 | CSCI 225 sec 18 |
| 22199 | CSCI 237 sec FLEX |
| 22200 | CSCI 250 sec 16 |
| 22201 | CSCI 275 sec 15H |
| 22204 | ECON 101 sec 15 |
| 22208 | ECON 103 sec 11 |
| 22211 | ECON 105 sec 17 |
| 22212 | ECON 207 sec FLEX |
| 22362 | ECON 240 sec 13 |
| 22218 | ENGL 099 sec 10 |
| 22220 | ENGL 099 sec 12 |
| 22222 | ENGL 100 sec 101H |
| 22223 | ENGL 100 sec 10H |
| 22224 | ENGL 100 sec 11 |
| 22225 | ENGL 100 sec 12H |
| 22227 | ENGL 100 sec 13 |
| 22228 | ENGL 100 sec 141 |
| 22229 | ENGL 100 sec 14H |
| 22234 | ENGL 100 sec 15H |
| 22230 | ENGL 100 sec 16H |
| 22235 | ENGL 100 sec 17H |
| 22232 | ENGL 100 sec 18 |
| 22226 | ENGL 100 sec 42H |
| 22233 | ENGL 100 sec 45 |
| 22237 | ENGL 100 sec 48H |
| 22231 | ENGL 100 sec 8H |
| 22238 | ENGL 100 sec 9H |
| 22242 | ENGL 108 sec 08 |
| 22239 | ENGL 108 sec 10 |
| 22241 | ENGL 108 sec 121S |
| 22240 | ENGL 108 sec 13 |
| 22243 | ENGL 108 sec 15 |
| 22247 | ENGL 110 sec 11 |
| 22245 | ENGL 110 sec 14 |
| 22246 | ENGL 110 sec 16 |
| 22353 | ENGL 131 sec 12 |
| 22359 | ENGL 231 sec 99 |
| 22356 | FM 10 sec 12 |
| 22252 | GEOG 100 sec 8 |
| 22253 | GEOG 104 sec 141 |
| 22255 | GEOG 111 sec 17 |
| 22254 | GEOG 111 sec 8 |
| 22256 | GEOG 200 sec FLEX |
| 22257 | GEOG 230 sec 14 |
| 22258 | GEOG 255 sec 12 |
| 22260 | HIST 110 sec 101 |
| 22259 | HIST 110 sec 11 |
| 22262 | HIST 120 sec 12 |
| 22264 | HIST 120 sec 17 |
| 22265 | HIST 202 sec 141 |
| 22266 | HIST 209 sec 10 |
| 22355 | HIST 211 sec 16 |
| 22267 | HIST 212 sec 18 |
| 22369 | HSCI 130 sec 14 |
| 22374 | HSCI 130L sec 1414 |
| 22270 | MATH 100 sec 16 |
| 22271 | MATH 100 sec 17 |
| 22272 | MATH 105 sec 19 |
| 22273 | MATH 110 sec 12 |
| 22276 | MATH 111 sec 15 |
| 22278 | MATH 113 sec 12 |
| 22281 | MATH 114 sec 13 |
| 22280 | MATH 114 sec 141 |
| 22282 | MATH 115 sec 17 |
| 22284 | MATH 120 sec 11 |
| 22367 | MATH 120 sec 14 |
| 22285 | MATH 206 sec 11 |
| 22286 | MATH 213 sec 14 |
| 22383 | MATH 214 sec 99 |
| 22288 | MATH 225 sec 19 |
| 22289 | MATH 230 sec 18 |
| 22290 | MATH 252 sec 161 |
| 22358 | PGEO 12 sec 10 |
| 22293 | PHIL 101 sec 10 |
| 22294 | PHIL 102 sec 11 |
| 22295 | PHIL 113 sec 13 |
| 22298 | PHIL 213 sec 141 |
| 22370 | PHIL 260 sec 9 |
| 22299 | PHYS 100 sec 11H |
| 22300 | PHYS 100L sec 115 |
| 22302 | PHYS 110 sec 10 |
| 22303 | PHYS 110L sec 1014 |
| 22306 | PHYS 120 sec 15 |
| 22307 | PHYS 120L sec 1414 |
| 22375 | PHYS 210 sec 99 |
| 22376 | PHYS 210L sec 124 |
| 22311 | PSCI 100 sec 10 |
| 22312 | PSCI 100 sec 121 |
| 22314 | PSCI 100 sec 17 |
| 22317 | PSCI 101 sec 15 |
| 22318 | PSCI 101 sec 16 |
| 22321 | PSCI 202 sec 11 |
| 22320 | PSCI 202 sec 14 |
| 22361 | PSCI 210 sec 101 |
| 22323 | PSCI 210 sec FLEX |
| 22364 | PSCI 220 sec 161 |
| 22325 | PSCI 240 sec 13 |
| 22365 | PSCI 251 sec FLEX |
| 22366 | PSCI 252 sec 12 |
| 22327 | PSCI 260 sec 8 |
| 22328 | PSCI 275 sec FLEX |
| 22332 | PSYC 110 sec 12 |
| 22334 | PSYC 110 sec 121 |
| 22335 | PSYC 110 sec 16 |
| 22338 | PSYC 120 sec 10 |
| 22337 | PSYC 120 sec 11 |
| 22339 | PSYC 217 sec 13 |
| 22340 | PSYC 218 sec 8 |
| 22342 | PSYC 240 sec 101 |
| 22343 | PSYC 281 sec 9 |
| 22344 | SOCI 110 sec 13 |
| 22347 | SOCI 110 sec 18 |
| 22348 | SOCI 120 sec 12 |
| 22349 | SOCI 230 sec 14 |
| 22350 | SOCI 250 sec 17 |

⚙️ The course ID list can be modified directly in the script, or automatically generated (see next section).

---

## 🛠️ Planned Add-on: Course Metadata Generator

You can add a helper script (`generate_courses_md.py`) to fetch and update course IDs and names each semester, then regenerate a Markdown table like the one above. This helps you keep your tracking list fresh with no manual effort.

---

## 📱 Bonus Setup: BuzzKill for Supercharged Phone Alerts (Android)

> Combine Pushbullet + [BuzzKill](https://play.google.com/store/apps/details?id=com.samruston.buzzkill) to turn your phone into a **seat-hunting alarm system**.

- Trigger custom actions (vibrate, speak text, flash, siren) when the message contains keywords like "Seats Available"
- Make your phone impossible to ignore when a seat opens up!

# 🛠️ Step-by-Step: Use BuzzKill with Pushbullet

✅ 1. **Install BuzzKill**
- [📥 Google Play Store link](https://play.google.com/store/apps/details?id=com.samruston.buzzkill)
- Free trial available; worth it for full control if you're serious about alerts.

✅ 2. **Give BuzzKill Permissions**
When you open the app:
- Allow **Notification Access**
- Allow **Do Not Disturb access** (for overriding silent mode)
- Enable **Battery optimizations off** (so it always runs)

✅ 3. **Create a New BuzzKill Rule for Pushbullet**

1. Tap `➕` (add new rule)
2. Choose **App** → Select **Pushbullet**
3. Choose **"Notification Contains Text"**
4. In the text field, type something like:
   ```
   Course Seats Alert
   ```
   or even just `"Seats"` to trigger on anything seat-related

---

## 🛡️ Disclaimer

This script is provided for educational/personal use. Use responsibly. API endpoints may change without notice.

---

## 👨‍💻 Author

Created with ❤️ by Arsh

---

## 📜 License

MIT License
```
