
from selenium import webdriver
 #driver = webdriver.Chrome('C:/chromedriver.exe')
from email import encoders
from email import encoders

from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.message import EmailMessage
import smtplib
import time
import os

smtplibObj = smtplib.SMTP("smtp.gmail.com", 587)
smtplibObj.ehlo()
smtplibObj.starttls()
smtplibObj.login("myemail@gmail.com","password")
filename = "mFleet2.pdf"
smtplibObj.sendmail("myemail@gmail.com", "sendto@gmail.com","Subject:Hello\nBonjour\n")
message = MIMEMultipart("alternative")

app_pass = "password"
host_user = "myemail@gmail.com"
msg = EmailMessage()
msg['From'] = host_user
msg['To'] = host_user
msg['Subject'] = "HOW"
msg.set_content("good")

msg = MIMEMultipart()
msg['From'] = 'myemail@gmail.com'
msg['To'] = 'sendto@gmail.com'
msg['Subject'] = 'Robot Uprising'
message = 'We are coming for you!'
msg.attach(MIMEText(message))

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\

"""
print("Hello.")
time.sleep(3)
print ("It's been three seconds since we said hello.")

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                    '<a href="http://www.python.org">link</a>'+
'<p><img src="cid:0"></p>' +
'</body></html>', 'html', 'utf-8'))

smtplibObj.quit()
