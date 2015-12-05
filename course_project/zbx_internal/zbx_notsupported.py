#!/usr/bin/python3.5
# coding: UTF-8

import MySQLdb
import os
import smtplib
from config import *

# DB select:
db_select = """SELECT host, count(itemid) FROM hosts LEFT JOIN items ON
                items.hostid = hosts.hostid AND items.state = 1 AND items.status = 0 AND items.flags !=4
                WHERE hosts.status != 1 AND hosts.host NOT LIKE '%emplate%' GROUP BY hosts.host;"""

try:
    #Connect to Zabbix DB:
    con = MySQLdb.connect(host=cfg_host, user=cfg_user, passwd=cfg_passwd, db=cfg_db)
    cur = con.cursor()

    #Take Unsupported items row[1] & hostnames row[0]:
    cur.execute(db_select)
    result = cur.fetchall()

    for row in result:

        #For debug:
        #print(row[0], row[1])

        #Now send values to zabbix, using zabbix-sender binary:
        command = ('{} -z {} -p {} -s {} -k {} -o {}'.format(zsbin, serv, port, zkey, row[0], row[1]))
        os.system(command)

except MySQLdb.Error:
    print(db.error())


    server = smtplib.SMTP(mail_serv, mail_port)
    server.ehlo()
    server.starttls()
    server.login(mail_usr, mail_pwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % mail_usr,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(mail_usr, [TO], BODY)
        print ('Email sent.')
    except:
        print ('Error sending mail.')

    server.quit()