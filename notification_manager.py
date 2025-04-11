
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    """Responsible for sending notifications via email."""
    def __init__(self):
        self.email = os.getenv("EMAIL_SENDER")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.recipient = os.getenv("EMAIL_RECIPIENT")

    def send_email(self, subject, message_body):
        full_message = f"Subject:{subject}\n\n{message_body}"

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(self.email, self.password)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=self.recipient,
                    msg=full_message.encode("utf-8")
                )
                print("Simple email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
