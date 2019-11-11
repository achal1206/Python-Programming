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
message = "hi"

# sending the mail 
s.sendmail("achal.16it@cmr.edu.in", "jainachal74@gmail.com", message) 

# terminating the session 
s.quit() 
'''
import smtplib
conn = smtplib.SMTP('imap.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('youremail@gmail.com', 'your_password')

conn.sendmail('from@gmail.com','to@gmail.com','Subject: What you like? \n\n Reply Reply Reply')
conn.quit()
'''
