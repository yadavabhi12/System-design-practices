class EmailService:
    """
    Low-level module
    Responsible for sending emails
    """

    def send_email(self, message):
        print(f"Email Sent: {message}")


class Notification:
    """
    High-level module

    Directly depends on EmailService
    """

    def __init__(self):
        self.email_service = EmailService()

    def send(self, message):
        self.email_service.send_email(message)


notification = Notification()
notification.send("Welcome User")









# Problem 1
# Notification tightly coupled with EmailService

# Problem 2
# If tomorrow we want SMS
# We must modify Notification class

# Problem 3
# Hard to test

# Problem 4
# Not scalable

# Problem 5
# Violates DIP