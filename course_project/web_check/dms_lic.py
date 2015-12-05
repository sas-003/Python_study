#!/usr/bin/python2.6
# coding: UTF-8

import re
import requests
import sys
import json
import time
from config import *

try:
    response1 = requests.get(url_login, timeout=timeout)
    if response1.status_code != 200:
        raise ValueError('1')
    csrftoken = response1.cookies['csrftoken']

    data = {
        'csrfmiddlewaretoken': csrftoken,
        'username': web_user,
        'password': web_pass,
    }
    cookies = {
        'csrftoken': csrftoken,
    }
    response2 = requests.post(url_login, data=data, cookies=cookies, allow_redirects=False, timeout=timeout)
    if response2.status_code != 302:
        raise ValueError('2')
    sessionid = response2.cookies['sessionid']

    cookies = {
        'csrftoken': csrftoken,
        'sessionid': sessionid,
    }

    headers = {
        'X-Requested-With': 'XMLHttpRequest',
    }

    response3 = requests.get(url_licenses, cookies=cookies, timeout=timeout, headers=headers)

    if response3.status_code != 200:
        raise ValueError('3')

    x = json.loads(response3.text)
    endtime = x["parameters"][1]["value"]
    print int(time.mktime(time.strptime(endtime, '%Y-%m-%d')))

except ValueError:
    print '1' #case1
except requests.exceptions.ConnectionError:
    print '2' #case2
