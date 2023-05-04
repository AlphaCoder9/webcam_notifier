import smtplib
from email.message import EmailMessage
import imghdr
import os

# Stored passcode inside of env variable using OS.
PASSWORD = os.getenv("PASSWORD")
SENDER = "adeelta302@gmail.com"
RECEIVER = "adeelta302@gmail.com"


# Mapping def to main.py
def send_email(img_path):
    print("SENT E-MAIL HAS STARTED... ")
    email_message = EmailMessage()
    email_message["Subject"] = "ALERT! *Movement Detected*"
    email_message.set_content("New object found!")

    with open(img_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    # setting up Google server. NOTE: if VPN is enabled it might not work. ll have to workaround.
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("SENT EMAIL HAS ENDED. ")  # Message to display on Terminal.

# if __name__ == "__main__":
#     send_email(img_path="images/image001.png")
