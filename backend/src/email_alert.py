
"""import smtplib
from email.message import EmailMessage
import os

def send_email(video_path):
    sender = "dhanalakshmiavidi30@gmail.com"
    password = "vlzv ovsm gjkb gwad"
    receiver = "dhanalakshmiavidi30@gmail.com"

    msg = EmailMessage()
    msg['Subject'] = "🚨 Drowsiness Alert"
    msg['From'] = sender
    msg['To'] = receiver

    msg.set_content("Driver is drowsy. Video attached.")

    with open(video_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(video_path)

    msg.add_attachment(file_data,
                       maintype='video',
                       subtype='mp4',
                       filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("✅ Email Sent Successfully")
    except Exception as e:
        print("❌ Email Error:", e)"""


import smtplib
from email.message import EmailMessage
import os

def send_email(video_path):

    sender = "dhanalakshmiavidi30@gmail.com"
    password = os.getenv("GMAIL_APP_PASSWORD")
    receiver = "dhanalakshmiavidi30@gmail.com"

    if not password:
        print("Email Error: Gmail App Password not configured")
        return

    if not os.path.exists(video_path):
        print("Email Error: Video file not found")
        return

    msg = EmailMessage()
    msg['Subject'] = "Drowsiness Alert"
    msg['From'] = sender
    msg['To'] = receiver

    msg.set_content(
        "Driver is drowsy. Please check the attached video."
    )

    with open(video_path, 'rb') as f:
        file_data = f.read()

    file_name = os.path.basename(video_path)

    msg.add_attachment(
        file_data,
        maintype='video',
        subtype='mp4',
        filename=file_name
    )

    try:
        with smtplib.SMTP_SSL(
            'smtp.gmail.com', 465, timeout=30
        ) as smtp:

            smtp.login(sender, password)
            smtp.send_message(msg)

        print("Email Sent Successfully!")

    except Exception as e:
        print("Email Error:", repr(e))
