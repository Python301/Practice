# Send Email Program

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your email credentials
sender_email = "yedukondalu716@gmail.com"
receiver_email = "yedukondalu.bhyrisetti@engro.io"
password = "ljgc jldg aqms quqt"  # Use Gmail App Password here

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Scraping Alert!!!!"

# Email body
body = """\
Hey,

I Am From The Cron Job Setup.

Love,
B.Yedukondalu
"""

# Attach the body to the message
message.attach(MIMEText(body, "plain"))

# Send the email using Gmail's SMTP server
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully! 💌")
except Exception as e:
    print("Failed to send email. ❌")
    print(f"Error: {e}")
