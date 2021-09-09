#coding=utf-8
import pdfkit
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders

config = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_url('https://tets.com/index.php?module=index.php', 'out.pdf',configuration=config)
