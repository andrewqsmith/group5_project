import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

class EmailSender:
   def __init__(self, from_email, password, to_email, subject, body):
       self.from_email = from_email
       self.password = password
       self.to_email = to_email
       self.subject = subject
       self.body = body

   def send_email(self):
       msg = MIMEMultipart()
       msg['From'] = self.from_email
       msg['To'] = self.to_email
       msg['Subject'] = self.subject
       msg.attach(MIMEText(self.body, 'plain'))
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.starttls()
       server.login(self.from_email, self.password)
       text = msg.as_string()
       server.sendmail(self.from_email, self.to_email, text)
       server.quit()
	   
	def purchase_made():
	   # Code for making a purchase goes here
	   email_sender = EmailSender('your-email@gmail.com', 'your-password', 'customer-email@gmail.com', 'Purchase Confirmation', 'Your purchase has been confirmed.')
	   schedule.every(5).minutes.do(email_sender.send_email)

	while True:
	   schedule.run_pending()
	   time.sleep(1)
