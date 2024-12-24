import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_phishing_email(recipient_email):
    # Email credentials
    sender_email = "phishing.simulator@example.com"
    sender_password = "password123"  # Use a secure method for real credentials
    subject = "Urgent: Verify Your Account"

    # Phishing email content
    html_content = """
    <html>
    <body>
        <p>Dear user,</p>
        <p>We noticed unusual activity in your account. Please click the link below to verify:</p>
        <a href="http://127.0.0.1:5000/login">Verify Now</a>
        <p>Thank you,</p>
        <p>Your Security Team</p>
    </body>
    </html>
    """
    # Email setup
    msg = MIMEMultipart("alternative")
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(html_content, "html"))

    try:
        # Connect to SMTP server and send email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Phishing email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
send_phishing_email("victim@example.com")
