# 📧 Resume Email Automation (Python)

A powerful **Python automation script** jo **bulk job application emails** send karta hai 📤
Resume attach hota hai 📄, Excel se data read hota hai 📊, aur status auto-track hota hai ✅

Perfect hai **job hunting automation**, **daily HR reach-out**, aur **time saving** ke liye ⏱️🔥

---

## 🚀 Features

* 📧 Bulk job application email sending
* 📄 Resume attachment support (PDF)
* 📊 Excel-based company & HR email management
* 🧠 Dynamic email subject & body
* 🛑 **DRY RUN mode** (test without sending emails)
* ✅ Email status tracking (Sent / Error / Skipped)
* 💾 Automatic Excel backup generation
* 📁 Portable – runs from current project folder

---

## 📂 Project Structure

```
jobs/
│
├── Resume_Automation.py
├── jobs_list.xlsx
├── jobs_list_backup.xlsx   # auto-generated
├── resume.pdf
└── README.md
```

---

## 📊 Excel File Format (`jobs_list.xlsx`)

### 🔹 Required Columns

| Column Name | Required | Description          |
| ----------- | -------- | -------------------- |
| CompanyName | ✅ Yes    | Company ka naam      |
| HR_Email    | ✅ Yes    | HR / Recruiter email |

### 🔹 Optional Columns (Auto-Handled)

| Column Name | Required | Description               |
| ----------- | -------- | ------------------------- |
| Role        | ❌ No     | Job role                  |
| Location    | ❌ No     | Job location              |
| Status      | ❌ No     | Script auto-update karega |

📌 **Note:**
Agar `Status = Sent` hoga to email dobara nahi jayega 🚫📧

---

## ⚙️ Configuration

`Resume_Automation.py` file me niche diye gaye values update karo:

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_APP_PASSWORD = "your_gmail_app_password"

DRY_RUN = False
MAX_EMAILS_PER_RUN = 150
```

⚠️ **Important:** Normal Gmail password use mat karo. Sirf **Gmail App Password** use karo.

---

## 🔐 How to Generate Gmail App Password

1. Google Account → **Security**
2. Enable **2-Step Verification**
3. Open **App Passwords**
4. Select:

   * App: Mail
   * Device: Other (Python Script)
5. Generate password
6. Script me paste karo ✅

---

## ▶️ How to Run the Script

Terminal / CMD me project folder open karke run karo:

```bash
python Resume_Automation.py
```

---

## 🧪 DRY RUN Mode (Recommended)

Testing ke liye pehle DRY RUN enable karo:

```python
DRY_RUN = True
```

📌 Is mode me:

* Koi real email send nahi hoga ❌
* Sirf logs print honge 🖨️
* Excel file safe rahegi 🔒

---

## 📝 Important Notes

* ⚠️ Gmail daily email sending limits apply hoti hai
* 📤 Recommended: **100–150 emails per day**
* 📄 Resume **PDF format** me hona chahiye
* 📁 Excel file aur resume script ke same folder me hone chahiye

---

## 👨‍💻 Author

**Jatin Rathod**
Python Automation Enthusiast 🤖
India 🇮🇳

---

## ⭐ Future Enhancements

* `.env` file support
* HTML email templates
* Command-line arguments
* Task Scheduler / Cron support
* LinkedIn job automation integration

---

🚀 **Happy Automating & Best of Luck for Your Job Search!**
