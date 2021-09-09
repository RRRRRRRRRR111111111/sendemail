
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders

file_path = r'C:\Users\khaled\Downloads\MFLEET.pdf'
print( os.path.isfile(file_path))


#for f in os.listdir("/home/khaled/python_error/docs/"):
	#print(f)

fromaddr = "rnoo.27soso@gmail.com"
toaddr = "rania.m.abdelkerim@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "subject"

body = ""

msg.attach(MIMEText(body, 'plain'))


#file_path = r'C:\Users\khaled\Downloads\MFLEET.pdf'
#part = MIMEBase('application', 'octet-stream')
#part.set_payload((attachment).read())
#encoders.encode_base64(part)
#part.add_header('Content-Disposition', "attachment; filename= %s" % file_path)

#msg.attach(part)
filename = 'MFLEET.pdf' #path t
fo=open(filename,'rb')
attach = MIMEApplication(fo.read(),_subtype="pdf")
fo.close()
attach.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(attach)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "rbppzxtvzrwsvicu")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
