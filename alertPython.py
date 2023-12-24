# can be used to send mail
import smtplib
# Creating email and MIME objects
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
def isServerDown(serverUrl):
    try:
        response = requests.get(serverUrl)
        return not response.ok
    except requests.RequestException:
        return True


def sendEmailNotification(senderEmail, receiverEmail, subject, message, smtpServer, smtpPort, smtpUsername, smtpPassword):

    emailMessage = MIMEMultipart()
    emailMessage['From'] = senderEmail
    emailMessage['To'] = receiverEmail
    emailMessage['Subject'] = subject

    emailMessage.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtpServer, smtpPort) as server:
        server.starttls() 
        server.login(smtpUsername, smtpPassword)
        server.sendmail(senderEmail, receiverEmail, emailMessage.as_string())

if __name__ == "__main__":
    serverUrlToCheck = "http://ali.com"
    if isServerDown(serverUrlToCheck):
        senderEmail = "ali@gmail.com"
        receiverEmail = "ali@yahoo.com"
        subject = "bad dwontime"
        message = "server need emergancy help"
        smtpServer = "smtp.gmail.com"
        smtpPort = 587
        smtpUsername = "ali@gmail.com"
        smtpPassword = "alipass"
        sendEmailNotification(senderEmail, receiverEmail, subject, message, smtpServer, smtpPort, smtpUsername, smtpPassword)
  