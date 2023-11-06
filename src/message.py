import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class Message:
    def __init__(self, sender, receiver, password):
        self.sender = sender
        self.receiver = receiver
        self.password = password

    def  read_csv(self, file_path='src/prices.csv'):
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
        return content


    def send_email(self):
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = 'Price Reached Target'

        body = self.read_csv()

        # Create an HTML message with the content from the CSV
        email_message = MIMEText(body, 'html')
        message.attach(email_message)

        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(self.sender, self.password)
        server.sendmail(self.sender, self.receiver, message.as_string())
        print('Email sent')
        server.quit()

message1 = Message('danielatest123@outlook.es', 'danielamoreno699@gmail.com', 'danielatestpython123456')
message1.send_email()