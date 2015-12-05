#!/usr/bin/python2.6
# coding: UTF-8

'''
Before use add to:
/etc/zabbix/zabbix_agentd.conf additional user parameter:
UserParameter=lic_end_time,python .../dms_lic.py 181

Need template: 18_DMS_license
Returns:
1 - incorrect returned status
2 - connection error / web unavailable
unixtime -  everything went fine
'''

#__________CONFIG STARTS__________________
url_root = r'http://XXX.XXX.XXX.XXX/login?next=/'
url_login = r'http://XXX.XXX.XXX.XXX/login?next=/'
url_licenses = r"http://XXX.XXX.XXX.XXX/ajax/license"
web_user = 'admin'
web_pass = '********'
timeout = 5
#__________CONFIG ENDS____________________