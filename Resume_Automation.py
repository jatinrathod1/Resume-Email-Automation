import os
import pandas as pd
import smtplib
from email.message import EmailMessage
from pathlib import Path

# ---------------- CONFIGURATION ---------------- #


BASE_DIR = Path(__file__).resolve().parent

EXCEL_PATH = BASE_DIR / "jobs_list.xlsx"
RESUME_PATH = BASE_DIR / "resume.pdf"

# Sender email (Gmail recommended)
SENDER_EMAIL = "jatinrathod@gmail.com"

# https://myaccount.google.com/apppasswords
# Gmail App Password (do NOT use normal Gmail password)
SENDER_APP_PASSWORD = ""

# SMTP settings for Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # SSL port

# DRY RUN:
# True  = simulate only (no real emails sent)
# False = send real emails
DRY_RUN = False

# Maximum emails allowed per run
MAX_EMAILS_PER_RUN = 150


# ---------------- EMAIL SUBJECT ---------------- #

def make_email_subject(company, role):
    """
    Generate dynamic subject line
    """
    if not role:
        role = "Full Stack Developer"
    return f"Application for {role} - {company}" if company else f"Application for {role}"


# ---------------- EMAIL BODY ---------------- #

def make_email_body(company, role, location):
    """
    Professional email body template
    """
    if not role:
        role = "Full Stack Developer"
    if not location:
        location = "your organization"
    if not company:
        company = "your organization"

    body = f"""
Dear Hiring Manager,

I hope you are doing well.

My name is Jatin Rathod and I am working as a Full Stack Developer
with around 1 year of hands-on experience in building and maintaining
web applications and backend services.

My skill set includes:
- Backend: Python / Node.js, REST APIs, database-driven applications
- Frontend: JavaScript, React
- Databases: SQL (queries, optimization, reporting)
- Other: automation scripts, integrations with Power BI and APIs

I am very interested in the {role} position at {company} ({location}) and believe
my experience can add value to your team.

Please find my resume attached for your review.

I would be happy to discuss how I can contribute to your projects.

Thank you for your time and consideration.

Best regards,
Jatin Rathod
Full Stack Developer
Ahmedabad, India
Contact: +91-XXXXXXXXXX
Email: {SENDER_EMAIL}
"""
    return body


# ---------------- LOAD EXCEL ---------------- #

def load_jobs(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Excel file not found: {path}")

    df = pd.read_excel(path)

    # Required columns
    required_cols = ["CompanyName", "HR_Email"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Optional columns
    for col in ["Role", "Location", "Status"]:
        if col not in df.columns:
            df[col] = ""
    # ✅ FORCE Status column to string type (fix pandas FutureWarning)
    df["Status"] = df["Status"].astype(str)

    return df


# ---------------- CREATE EMAIL ---------------- #

def create_email_row(row):
    company = str(row.get("CompanyName", "") or "").strip()
    to_email = str(row.get("HR_Email", "") or "").strip()
    role = str(row.get("Role", "") or "").strip()
    location = str(row.get("Location", "") or "").strip()

    if not to_email:
        return None

    subject = make_email_subject(company, role)
    body = make_email_body(company, role, location)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg.set_content(body)

    if not os.path.exists(RESUME_PATH):
        raise FileNotFoundError(f"Resume file not found: {RESUME_PATH}")

    with open(RESUME_PATH, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(RESUME_PATH)
        )

    return msg


# ---------------- MAIN FUNCTION ---------------- #

def send_bulk_emails():
    print("====================================================")
    print("               BULK RESUME SENDER v1.0               ")
    print("====================================================")
    print(f"Excel Path     : {EXCEL_PATH}")
    print(f"Resume Path    : {RESUME_PATH}")
    print(f"Sender Email   : {SENDER_EMAIL}")
    print(f"DRY_RUN        : {DRY_RUN}")
    print(f"MAX EMAILS RUN : {MAX_EMAILS_PER_RUN}")
    print("====================================================\n")

    print("Step 1: Loading Excel file...")
    df = load_jobs(EXCEL_PATH)
    print(f"Total rows in Excel: {len(df)}")

    smtp = None
    if not DRY_RUN:
        print("\nStep 2: Connecting to SMTP server...")
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
        print("SMTP login successful.\n")
    else:
        print("\nDRY_RUN is enabled. SMTP connection skipped.\n")

    sent_count = 0
    skipped_count = 0
    error_count = 0

    print("Step 3: Processing emails...\n")

    for idx, row in df.iterrows():

        if not DRY_RUN and sent_count >= MAX_EMAILS_PER_RUN:
            print("\nDaily sending limit reached.")
            break

        status = str(row.get("Status", "") or "").strip().lower()
        company = str(row.get("CompanyName", "") or "").strip()
        to_email = str(row.get("HR_Email", "") or "").strip()

        print("----------------------------------------------------")
        print(f"Row Index : {idx}")
        print(f"Company   : {company if company else '(not provided)'}")
        print(f"Email     : {to_email if to_email else '(not provided)'}")
        print(f"Status    : {status if status else '(blank)'}")

        if status == "sent":
            print("Action    : SKIPPED (already sent)")
            skipped_count += 1
            continue

        msg = create_email_row(row)
        if msg is None:
            print("Action    : SKIPPED (missing email)")
            skipped_count += 1
            continue

        print(f"Subject   : {msg['Subject']}")

        if DRY_RUN:
            print("Action    : DRY RUN (email not sent)")
            skipped_count += 1
        else:
            try:
                smtp.send_message(msg)
                print("Action    : SENT successfully")
                df.loc[idx, "Status"] = "Sent"
                sent_count += 1
            except Exception as e:
                print(f"Action    : ERROR -> {e}")
                df.loc[idx, "Status"] = f"Error: {e}"
                error_count += 1

    if smtp:
        smtp.quit()
        print("\nSMTP connection closed.")

    if not DRY_RUN:
        backup_path = EXCEL_PATH.with_name(
        EXCEL_PATH.stem + "_backup.xlsx"
    )

        print(f"\nSaving backup: {backup_path}")
        df.to_excel(backup_path, index=False)

        print(f"Updating Excel file: {EXCEL_PATH}")
        df.to_excel(EXCEL_PATH, index=False)

    print("\n==================== SUMMARY ====================")
    print(f"Total Rows : {len(df)}")
    print(f"Sent       : {sent_count}")
    print(f"Skipped    : {skipped_count}")
    print(f"Errors     : {error_count}")
    print(f"DRY_RUN    : {DRY_RUN}")
    print("=================================================\n")
    print("Process completed.")


# ---------------- ENTRY POINT ---------------- #

if __name__ == "__main__":
    send_bulk_emails()
