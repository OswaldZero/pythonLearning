from bs4 import BeautifulSoup
soup=BeautifulSoup('<p>hello</div>','lxml')
print(soup.p.string)
