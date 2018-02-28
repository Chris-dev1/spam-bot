# Email spam-bot by ChrissHack
# 

import smtplib
import platform
import getpass
import sys
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

email     = raw_input("Enter Your Email : ")
password  = getpass.getpass("Enter your Password:")

if not  email  and not password:
		print ("You must Login to your Gmail")
else:
		server.login(email,password)
		print ("Successfully Signed in")

		f = open('text', 'r')
		t = open('victim', 'r')
		html = f.read()

for line in t.readlines():

		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Hey!"
		msg['From'] = email
		msg['To'] = line
		text = "Hi!\nHow are you?\n"
		part1 = MIMEText(text, 'plain')
		part2 = MIMEText(html, 'html')
		msg.attach(part1)
		msg.attach(part2)
		server.sendmail(email,line,msg.as_string())
		print('Email for : 'line' sended!')
print ('All email sended! ')
server.quit()
f.close()
print(" ***Dedhack*** ")



