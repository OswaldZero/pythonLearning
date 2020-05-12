import requests
from bs4 import BeautifulSoup
url="http://coi.hzau.edu.cn"
res=requests.get(url)
res.encoding='utf-8'
soup=BeautifulSoup(res.text)
tag1=soup.find_all(div,class)