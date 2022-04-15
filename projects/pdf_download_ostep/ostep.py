import requests as req
from bs4 import BeautifulSoup as bsoup
import re
import urllib.request
import random

# download function
def download_file(url):
    dir_path = 'download/'
    rand = random.randint(1,100) + random.randint(1,100)*random.randint(1,100)
    file_name = dir_path + url.split('/')[-1]
    try:
        u = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print(url, 'url file not found')
        return
    print('Start downloading {0}, will be saved in {1}'.format(url.split('/')[-1],file_name))
    block_sz = 8192
    with open(file_name, 'wb') as f:
        while True:
            buffer = u.read(block_sz)
            if buffer:
                f.write(buffer)
            else:
                break
    print('Successful to download ', url.split('/')[-1])
    
    
    # Download
for i in range(1,51):
    if i < 10:
        page = '0' + str(i)
    else:
        page = str(i)
    url = 'https://pages.cs.wisc.edu/~remzi/OSTEP/Chinese/' + page + '.pdf'
    download_file(url) 