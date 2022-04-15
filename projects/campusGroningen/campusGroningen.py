from bs4 import BeautifulSoup as bsoup
from twilio.rest import Client
from datetime import datetime
import requests as req
import urllib.request
import random
import time
import re

#############################################################################
# Pre-Definition
AVAILABLE = 'Deelnemen'
FULL = 'Volgeboekt'

#############################################################################
# Functions
def blue_str(line):
    return ('\033[1;34m' + line + '\033[0m')

def green_str(line):
    return ('\033[1;32m' + line + '\033[0m')

def red_str(line):
    return ('\033[1;31m' + line + '\033[0m')

def check_status(url):
    r = req.get(url)
    if r.status_code == 200:
        soup = bsoup(r.text, 'html.parser')
        matchObj = re.search(AVAILABLE,str(soup))
        if matchObj is not None:
            print(green_str(url + ' is available!!'))
            return True
    return False

def sleeptime(hh, mm, ss):
    return hh * 3600 + mm * 60 + ss 

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_message(text, phone_number):
    account_sid = 'ACa9306ac012f900b31b72b00887a7f42a'
    auth_token = '3437533e1735f9083bc7e517c572e796'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=text,
                         from_='+19103487183',
                         to=phone_number
                     )

    print(message.sid)
    
#############################################################################
# Running
urls = []
with open('urls.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    urls.append(line)
f.close()

phone_numbers = ['+32489036909', '+31659372222']

print('--------------------------------------------------------')
print('Going to check this websites:')
for url in urls:
    print(url)
print('--------------------------------------------------------')

second = sleeptime(0, 0, 5)
is_find = False
while 1:
    print(datetime.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime("%H:%M:%S"))
    for url in urls:
        status = check_status(url)
        if status:
            for phone_number in phone_numbers:
                send_message("House Find!! Check URL:%s" % (url), phone_number)
            is_find = True
    if is_find:
        print(green_str("House Find!! Check URL:%s" % (url)))
        print('Program end.')
        break
    time.sleep(second)
