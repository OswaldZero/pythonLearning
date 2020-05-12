html="""
<html><head><title>Wuhan University</title></head>
<body>
<p class="kalof" name="university"><b>Wuhan University</b></p>
<p class="kalof">There are three universities, their names are:
<a href= "http://www.hust.edu.cn" class="hust" id="link1"><span>hust</span></a>
<a href= "http://www.ccnu.edu.cn" class="ccnu" id="link2" >ccnu</a>and
<a href= "http://www.hzau.edu.cn" class="hzau" id="link3">hzau</a>
and they are my learning universities</p>
<p class="kalof">...</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html, 'lxml' )
#一标签选择器Tag --> 4关联选择--> 4.1子节点和子孙节点
print(soup.contents)
print(soup.p.contents) # (1)获取直接子节点contents属性 
print( soup.p.children) # (2)获取子节点children属性
for i,child in enumerate(soup.p.children):
    print(i,child) 
print(soup.p.descendants) # (3)获取所有子孙节点descendants
for i,child in enumerate(soup.p.descendants): 
    print(i,child)
