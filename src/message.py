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

    def  read_csv(self, file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
            print(content)
        return content

    # def send_email(self):
    #     message = MIMEMultipart()
    #     message['From'] = self.sender
    #     message['To'] = self.receiver
    #     message['Subject'] = 'price reached target'

    #     body = self.read_csv(file_path='src/prices.csv')
        
    #     server = smtplib.SMTP('smtp.office365.com', 587)
    #     server.starttls()
    #     server.login(self.sender, self.password)
    #     server.sendmail(self.sender, self.receiver, body)
    #     server.quit()

