
import os
import smtplib

class NotificationManager:
    """Responsible for sending notifications via email."""
    def __init__(self):
        # Initialize the class with the sender's email, password, and recipient email.
        self.email = os.getenv("EMAIL_SENDER")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.recipient = os.getenv("EMAIL_RECIPIENT")

    def send_email(self, subject, message_body):
        # Construct the email message by including the subject and the body.
        full_message = f"Subject:{subject}\n\n{message_body}"

        try:
            # Establish a connection to the Gmail SMTP server.
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(self.email, self.password)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=self.recipient,
                    msg=full_message.encode("utf-8")
                )
                print("Simple email sent successfully!") # Print success message after sending the email
        except Exception as e:
            # If an error occurs, print the error message.
            print(f"Failed to send email: {e}")
