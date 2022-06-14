import requests
from urllib import request
from bs4 import BeautifulSoup
import re
import time
import os

st = time.time()
# connect to website and get list of all pdfs
url="https://www.menuiseries-bieber.com/dop/"
response = request.urlopen(url).read()
soup= BeautifulSoup(response, "html.parser")     
links = soup.find_all('a', href=re.compile(r'(.pdf)'))


# clean the pdf link names
url_lists = []
for el in links:
    if(el['href'].startswith('http')):
        url_lists.append(el['href'])
    else:
        url_lists.append("https://www.menuiseries-bieber.com/dop/" + el['href'])

#donload and name the pdf files
for url_list in url_lists:
    downloadUrl = url_list

    req = requests.get(downloadUrl)
    filename = req.url[downloadUrl.rfind('/')+1:]

    with open(filename, 'wb') as f:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    def download_file(url, filename=''):
        try:
            if filename:
                pass            
            else:
                filename = req.url[downloadUrl.rfind('/')+1:]

            with requests.get(url) as req:
                with open('/home/sofi/Desktop/aaaa/yoo/filename', 'wb') as f:
                    for chunk in req.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                return '/home/sofi/Desktop/aaaa/yoo/filename'
        except Exception as e:
            print(e)
            return None

et = time.time()
res = et - st
# final_res = res / 60


print('it took:', res, 'seconds to download')
