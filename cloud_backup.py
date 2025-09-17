import boto3
import os
from datetime import datetime
import logging
import smtplib
from email.message import EmailMessage

# Configure logging
logging.basicConfig(filename='logs/backup.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# AWS S3 setup
s3 = boto3.client('s3')
bucket_name = "my-backup-bucket"
local_backup_folder = "/home/user/data_to_backup/"

# AWS SNS or Email Notification Setup
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
TO_EMAIL = "notify_email@example.com"

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def upload_files():
    try:
        for root, dirs, files in os.walk(local_backup_folder):
            for file in files:
                local_path = os.path.join(root, file)
                s3_path = os.path.relpath(local_path, local_backup_folder)
                s3.upload_file(local_path, bucket_name, f"{datetime.now().strftime('%Y-%m-%d')}/{s3_path}")
                logging.info(f"Uploaded {file} to S3")
        send_email("Backup Success", "Automated backup completed successfully.")
    except Exception as e:
        logging.error(f"Backup failed: {e}")
        send_email("Backup Failed", f"Automated backup failed: {e}")

if __name__ == "__main__":
    upload_files()
