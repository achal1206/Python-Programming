# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 
from smtplib import SMTP
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.ehlo()
# start TLS for security 
s.starttls() 

# Authentication 
s.login("achal.16it@cmr.edu.in", "password") 

# message to be sent 
message = """\
Subject: Hi there

This message is sent from Python."""

# sending the mail 
s.sendmail("achal.16it@cmr.edu.in", "jainachal74@gmail.com", message) 

# terminating the session 
s.quit() 
