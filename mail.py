import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = "Container with this IP " + os.environ['IP'] + " has been attack"

#The mail addresses and password
sender_address = os.environ['MAIL']
sender_pass = os.environ['PASS']
receiver_address = os.environ['RECEIVER']
receiver_address2 = os.environ['RECEIVER2']

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address + "," + receiver_address2

message['Subject'] = "Alert 403-Forbidden Access Catalyst"   #The subject line

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.sendmail(sender_address, receiver_address2, text)
session.quit()
print('Mail Sent')