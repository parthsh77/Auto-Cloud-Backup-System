# Auto-Cloud-Backup-System



## Overview
This project automates the backup of critical files from a local server or EC2 instance to AWS S3. Features include versioning, lifecycle management, and email notifications for success/failure.

## Features
- Daily automated backup to S3
- S3 versioning and lifecycle rules
- AWS SNS email notifications
- Logging and monitoring via CloudWatch
- Cron job scheduling

## Tech Stack
- Python 3, Boto3
- AWS S3, IAM, SNS, CloudWatch
- Linux Cron for scheduling

## Usage
1. Configure AWS credentials using AWS CLI or environment variables.
2. Update `local_backup_folder` and `s3_bucket_name` in `cloud_backup.py`.
3. Install dependencies:
