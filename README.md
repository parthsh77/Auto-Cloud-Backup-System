```markdown
# ✅ Auto Cloud Backup System


## 📖 Project Overview

The **Automated Cloud Backup System** is a robust solution designed to securely back up critical files and databases from local servers or EC2 instances to **AWS S3**. The system ensures data protection through versioning, lifecycle management, automated scheduling, and real-time notifications using AWS services.

This project is ideal for **Cloud Administrator Interns**, DevOps engineers, or anyone interested in implementing reliable cloud-based backup solutions with minimal manual intervention.

---

## 🎯 Features

✔ Automatic daily backups to AWS S3  
✔ Versioning to maintain multiple backup states  
✔ Lifecycle management for cost-effective storage  
✔ Real-time notifications using AWS SNS  
✔ Monitoring using AWS CloudWatch  
✔ Secure credentials management with environment variables  
✔ Cron-based scheduling for automated execution  


---

## 📦 Requirements

Before using this project, ensure you have the following:

### ✅ Software
- Python 3.8 or higher  
- AWS CLI installed and configured  
- AWS IAM user with permissions for S3, SNS, and CloudWatch  

### ✅ Python Libraries  
Install dependencies using the following command:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```txt
boto3==1.31.0
python-dotenv==1.0.1
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/BEASTTech/Automated-Cloud-Backup-System.git
cd Automated-Cloud-Backup-System
```

### 2️⃣ Configure AWS Credentials

Set your AWS credentials using environment variables or a `.env` file:

Example `.env` file:

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
TO_EMAIL=notify_email@example.com
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Update Configuration

In `cloud_backup.py`, update the following parameters:

```python
local_backup_folder = "/path/to/your/data"
bucket_name = "your-s3-bucket-name"
```

### 5️⃣ Test the Backup Script

Run the script manually to ensure it's working:

```bash
python cloud_backup.py
```

### 6️⃣ Schedule Backups with Cron

Use the `cron_setup.txt` example to set up automated daily backups:

```bash
0 2 * * * /usr/bin/python3 /path/to/Automated-Cloud-Backup-System/cloud_backup.py
```

This schedules the backup to run every day at 2 AM.

### 📂 Folder for Logs

The `logs/` directory stores backup logs. Ensure this folder exists and has appropriate permissions:

```bash
mkdir logs
chmod 755 logs
```

---

## 📊 Architecture Diagram

The diagram below illustrates the flow of the system:

<img src="https://github.com/parthdummy/icons-main/blob/main/Diagram.png" width="500px">

**Flow Overview:**

1. Data from the Local Server or EC2 is picked up by the Backup Script.
2. Files are uploaded to AWS S3 with versioning enabled.
3. Lifecycle rules transfer old backups to AWS Glacier for cost savings.
4. AWS CloudWatch monitors performance and logs.
5. AWS SNS sends real-time notifications to email or Slack.

---

## 📥 Example .env Template

Create a file named `.env` in your project folder and paste the following:

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
TO_EMAIL=notify_email@example.com
```

Replace the placeholders with your actual AWS credentials and notification settings.

---

## ✅ Usage Tips

✔ Use environment variables to store sensitive information.  
✔ Test the backup process manually before scheduling.  
✔ Monitor logs regularly to ensure backups are running smoothly.  
✔ Enable lifecycle rules in S3 to reduce storage costs.  
✔ Use CloudWatch dashboards to track performance and error alerts.  

---

## 📂 Future Enhancements

✔ Support for multiple AWS regions  
✔ Encrypted backups with AWS KMS  
✔ Integration with Slack for notifications  
✔ GUI dashboard for easier management  
✔ Containerization with Docker for portability  

---

## 📬 Contact

If you have questions or want to collaborate, feel free to open an issue or reach out.

---
