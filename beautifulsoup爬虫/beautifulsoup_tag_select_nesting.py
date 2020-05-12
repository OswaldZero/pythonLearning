html="""
<html><head><title>The Dormouse's story</title></head>
<body>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
#一标签选择器Tag
# 3嵌套选择
print(soup.head.title)
print(type(soup.head.title) )
print(soup.head.title.string)
