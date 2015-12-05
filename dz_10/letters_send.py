# coding: utf-8

# SENDING

import smtplib

# Letter details
TO = 'gruppa9711529@gmail.com' #'domahes@yandex.ru'
SUBJECT = 'Greetings from python study group.'
TEXT = 'Here is a message from python.'

# Gmail credentials
gmail_usr = 'gruppa9711529@gmail.com'
gmail_pwd = 'efqkpnvbqwetssts'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_usr, gmail_pwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_usr,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_usr, [TO], BODY)
    print ('Email sent.')
except:
    print ('Error sending mail.')

server.quit()