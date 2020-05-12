html= """
<html>
    <head>
        <title>Wuhan University</title>
    </head>
    <body>
        <p class="nice" name='wyh'>hzau</>
    </body>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup (html,'lxml')
#一标签选择器Tag
# 1选择元素
print(soup.p) # p是htm1标签元素
print(type(soup.p))
# 2提取信息
print (soup.p.name)
#(1)获取名称name属性
print(soup.p.attrs)
# (2)获取属性attrs
print( soup.p.attrs['class'][0])
print( soup.p.attrs['name'] )
print(soup.p.string)
# (3) 获取内容string属性
