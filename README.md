# Bulk Resume Email Automation (Python)

A Python automation script to send job application emails in bulk with your resume attached.
The script reads company and HR email details from an Excel file, sends personalized emails,
tracks the status, and creates automatic backups.

---

## 🚀 Features

- 📧 Bulk job application email sending
- 📄 Resume attachment support (PDF)
- 📊 Excel-based company & HR email management
- 🧠 Dynamic email subject and body
- 🛑 DRY RUN mode (test without sending emails)
- ✅ Email status tracking (Sent / Error)
- 💾 Automatic Excel backup generation
- 📁 Portable – runs from current project folder

---

## 📂 Project Structure

jobs/
│
├── Resume_Automation.py
├── jobs_list.xlsx
├── jobs_list_backup.xlsx (auto-generated)
├── resume.pdf
└── README.md

yaml
Copy code

---

## 📊 Excel File Format (`jobs_list.xlsx`)

Required columns:

| Column Name   | Required | Description |
|--------------|----------|-------------|
| CompanyName  | ✅ Yes   | Company name |
| HR_Email     | ✅ Yes   | HR / Recruiter email |
| Role         | ❌ No    | Job role |
| Location     | ❌ No    | Job location |
| Status       | ❌ No    | Auto-updated by script |

---

## ⚙️ Configuration

Update the following values inside `Resume_Automation.py`:

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_APP_PASSWORD = "your_gmail_app_password"
DRY_RUN = False
MAX_EMAILS_PER_RUN = 150
⚠️ Important:
Use Gmail App Password, not your normal Gmail password.

🔐 How to Generate Gmail App Password
Open Google Account → Security

Enable 2-Step Verification

Go to App Passwords

Select:

App: Mail

Device: Other (Python Script)

Generate and copy the password

Paste it into the script

▶️ How to Run the Script
Open terminal / CMD inside the project folder and run:

bash
Copy code
python Resume_Automation.py
🧪 DRY RUN Mode (Recommended for Testing)
To test without sending real emails:

python
Copy code
DRY_RUN = True
This will simulate email sending and print logs only.

📝 Important Notes
Gmail daily email sending limits apply

Recommended: 100–150 emails per day

Resume must be in PDF format

Excel file and resume must be in the same folder as the script

👨‍💻 Author
Jatin Rathod
Python Automation Enthusiast
India 🇮🇳

⭐ Future Enhancements
Environment variable (.env) support

HTML email templates

Command-line arguments

Task Scheduler / Cron support

LinkedIn job automation integration
