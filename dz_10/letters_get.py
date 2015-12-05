# coding: utf-8

# GETTING

import getpass, poplib

gmail_usr = 'gruppa9711529'
gmail_pwd = 'efqkpnvbqwetssts'
pop_server = 'pop.googlemail.com'
port = '995'

Mailbox = poplib.POP3_SSL(pop_server, port) 
Mailbox.user(gmail_usr) 
Mailbox.pass_(gmail_pwd) 

numMessages = len(Mailbox.list()[1])

for i in range(numMessages):
    for msg in Mailbox.retr(i+1)[1]:
        print(msg)

Mailbox.quit()