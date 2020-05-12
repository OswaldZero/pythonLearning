#urllib
import urllib.request
from bs4 import BeautifulSoup
url='https://www.baidu.com'
html=urllib.request.urlopen(url)
bs=BeautifulSoup(html,'html.parser')
print(bs.prettify())
print(bs.get_text)
#requests
import requests
response=requests.get(url)
response.encoding='utf-8'
soup=BeautifulSoup(response.text)
print(soup.prettify())
print(soup.get_text())