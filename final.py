import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import random  # For simulating different scenarios

class EmailSender:
    def __init__(self, from_email, password, to_email):
        self.from_email = from_email
        self.password = password
        self.to_email = to_email

    def send_email(self, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.from_email, self.password)
        text = msg.as_string()
        server.sendmail(self.from_email, self.to_email, text)
        server.quit()

    def send_success_email(self):
        subject = "Purchase Successful"
        body = "Your purchase was successful."
        self.send_email(subject, body)

    def send_failure_email(self):
        subject = "Purchase Unsuccessful"
        body = "Your purchase was unsuccessful."
        self.send_email(subject, body)

    def send_storage_available_email(self):
        subject = "Storage Available"
        body = "Storage space is available for your request."
        self.send_email(subject, body)

    def send_storage_unavailable_email(self):
        subject = "Storage Unavailable"
        body = "Unfortunately, storage space is not available at the moment."
        self.send_email(subject, body)

def simulate_scenarios(email_sender):
    # Randomly decide the scenario
    scenario = random.choice(['purchase_success', 'purchase_failure', 'storage_available', 'storage_unavailable'])
    
    if scenario == 'purchase_success':
        email_sender.send_success_email()
    elif scenario == 'purchase_failure':
        email_sender.send_failure_email()
    elif scenario == 'storage_available':
        email_sender.send_storage_available_email()
    else:
        email_sender.send_storage_unavailable_email()

# Initialize EmailSender with your email credentials
email_sender = EmailSender('your-email@gmail.com', 'your-password', 'customer-email@gmail.com')

# Schedule the scenario simulation to run every 5 minutes
schedule.every(5).minutes.do(simulate_scenarios, email_sender)

while True:
    schedule.run_pending()
    time.sleep(1)
