"""
Before you run this code, make sure to do the following:

    Enable "Less secure apps" on your Gmail account if you're using Gmail.
    Note that this method is not recommended for sensitive accounts,
    as it involves storing your email and password in your code.

    If you have two-factor authentication enabled on your Gmail account,
    you might need to generate an "App Password" and use it as your EMAIL_PASSWORD.

    Replace the placeholders with your actual Gmail email address and password,
    as well as the recipient's email address.

    Make sure your MicroPython device is connected to the internet and has
    the necessary network configuration.

Please be cautious when storing your email credentials in code,
as it can pose security risks. Using OAuth2 or a more secure authentication method is recommended
for production use cases. This example is for educational purposes only and should not
be used in production systems without proper security measures.

Δεν υπάρχει το smtplib μπορώ να δωκιμάσω το uMail https://github.com/shawwwn/uMail

"""
from credentials import secrets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config  # Import the credentials from config.py

def send_email(subject, body):
    # Create a message
    msg = MIMEMultipart()
    msg['From'] = secrets["EMAIL_ADDRESS"]  # Use the imported email address
    msg['To'] = secrets["to_email"]
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Establish an SMTP connection and send the email
    try:
        server = smtplib.SMTP(secrets["SMTP_SERVER"], secrets["SMTP_PORT"])
        server.starttls()  # Use TLS (Transport Layer Security) for encryption
        server.login(secrets["EMAIL_ADDRESS"], secrets["EMAIL_PASSWORD"])  # Use the imported credentials
        text = msg.as_string()
        server.sendmail(secrets["EMAIL_ADDRESS"], secrets["to_email"], text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error: unable to send email -", str(e))

# Example usage:
#subject = "Test Email"
#body = "This is a test email sent from MicroPython."
#send_email(subject, body)