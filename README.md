# 📧 Resume Email Automation (Python)

A powerful **Python automation script** designed to send **bulk job application emails** with your resume attached.
The script reads company and HR details from an Excel file, sends personalized emails, tracks delivery status, and automatically creates backups.

This project is ideal for **job seekers**, **automation enthusiasts**, and anyone looking to save time while applying for multiple roles.

---

## 🚀 Features

* 📧 Bulk job application email sending
* 📄 Resume attachment support (PDF)
* 📊 Excel-based company & HR email management
* 🧠 Dynamic email subject and body generation
* 🛑 **DRY RUN mode** (test without sending real emails)
* ✅ Email status tracking (Sent / Error / Skipped)
* 💾 Automatic Excel backup generation
* 📁 Portable – runs directly from the project folder

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

### Required Columns

| Column Name | Required | Description                   |
| ----------- | -------- | ----------------------------- |
| CompanyName | Yes      | Name of the company           |
| HR_Email    | Yes      | HR or Recruiter email address |

### Optional Columns (Handled Automatically)

| Column Name | Required | Description                         |
| ----------- | -------- | ----------------------------------- |
| Role        | No       | Job role or position                |
| Location    | No       | Job location                        |
| Status      | No       | Automatically updated by the script |

📌 **Note:**
If the `Status` value is `Sent`, the script will skip that row and will not send the email again.

---

## ⚙️ Configuration

Update the following values inside the `Resume_Automation.py` file:

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_APP_PASSWORD = "your_gmail_app_password"

DRY_RUN = False
MAX_EMAILS_PER_RUN = 150
```

⚠️ **Important:** Do not use your normal Gmail password. Always use a **Gmail App Password**.

---

## 🔐 How to Generate a Gmail App Password

1. Open your **Google Account** → **Security**
2. Enable **2-Step Verification**
3. Go to **App Passwords**
4. Select:

   * App: Mail
   * Device: Other (Python Script)
5. Generate the password
6. Copy and paste it into the script

---

## ▶️ How to Run the Script

Open Terminal / Command Prompt in the project folder and run:

```bash
python Resume_Automation.py
```

---

## 🧪 DRY RUN Mode (Recommended for Testing)

Before sending real emails, it is recommended to enable DRY RUN mode:

```python
DRY_RUN = True
```

In this mode:

* No real emails are sent
* All actions are logged in the console
* Your Excel file remains unchanged

---

## 📝 Important Notes

* Gmail daily email sending limits apply
* Recommended limit: **100–150 emails per day**
* Resume must be in **PDF format**
* Excel file, resume, and script must be in the same project folder

---

## 👨‍💻 Author

**Jatin Rathod**
Python Automation Enthusiast
India 🇮🇳

---

## ⭐ Future Enhancements

* Environment variable support (`.env`)
* HTML email templates
* Command-line arguments
* Task Scheduler / Cron integration
* LinkedIn job automation integration

---

🚀 **Happy Automating and Best of Luck with Your Job Search!**
