#

import requests as req
from bs4 import BeautifulSoup as bsoup
import re
import urllib.request

def download_file(url):
    dir_path = 'download/'
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


def url_download(url):
    r = req.get(url)
    if r.status_code == 200:
        soup = bsoup(r.text, 'html.parser')
        pdf = soup.find(id='pdf')
        url = re.findall(r'.*\.pdf',pdf.get('src'))[0]
        if(not re.search('https',url)):
            url = 'https:' + url
        download_file(url)
    else:
        print ('errors occur.') 


# import files
print('Initializing...')
print('Initiliazation finished.')
print('Importing dois.txt...')
dois = []
with open('dois.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    dois.append(line)
f.close()
print('Import dois.txt finished.')
print('Start downloading...')

base = 'https://sci-hub.hkvisa.net/'
for doi in dois:
    url = base + doi
    url_download(url)

print('All download finished!')
print('Program finished!')
