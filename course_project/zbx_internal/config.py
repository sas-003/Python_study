#!/usr/bin/python3.5
# coding: UTF-8

'''
Before use:
Cron: 00 * * * * /usr/local/bin/python3.5 /home/zhukov/project_unsupported/main.py

Need Template: 00_Unsupported_items
Returns:
'''

#__________CONFIG STARTS__________________
# Letter details
TO = 'admin@work.com'
SUBJECT = 'Zabbix supported-items-check FAILED!.'
TEXT = 'Zabbix server, cron script error. DB connection error.'

# Mail credentials
mail_ser = 'smtp.work.com'
mail_port = 587
mail_usr = 'zabbix@work.com'
mail_pwd = '******'

#Server parameters:
zsbin = '/usr/bin/zabbix_sender'
serv = 'localhost'
port = '10051'
zkey = 'unsupported_items'

# DB credentials:
cfg_host="localhost",
cfg_user="root",
cfg_passwd="*****",
cfg_db="zabbix"
#__________CONFIG ENDS____________________