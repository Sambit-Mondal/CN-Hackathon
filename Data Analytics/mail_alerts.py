# mail_alerts.py
import smtplib
from email.mime.text import MIMEText

# Gmail SMTP configuration – update these with your details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL = "youremail@gmail.com"    # Your Gmail address
SENDER_PASSWORD = "yourpassword"          # Your Gmail password or app-specific password

def send_email_notification(subject, body, recipient_email):
    """
    Sends an email notification with the provided subject and body.
    recipient_email: Email address of the user (the notification receiver)
    """
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False
