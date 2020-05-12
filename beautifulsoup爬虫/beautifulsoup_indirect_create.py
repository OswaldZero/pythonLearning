from bs4 import BeautifulSoup
a=open('beautifulsoup爬虫/test.html')
soup=BeautifulSoup(a)
print(soup.prettify())
