html="""
<html><head><title>Wuhan University</title></head>
<body>
<p class="kalof" name="university"><b>Wuhan University</b></p>
<p class="kalof">There are three universities, their names are:
<a href= "http://www.hust.edu.cn" class="hust" id="link1"><span>hust</span></a>
<a href= "http://www.ccnu.edu.cn" class="ccnu" id="link2" >ccnu</a>and
<a href= "http://www.hzau.edu.cn" class="hzau" id="link3">hzau</a>
and they are my learning universities</p>
<p class="kalof">
    <a herf="http://www.hzau.edu.cn">hzau
        <span>h</span>
    </a>
</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
#一标签选择器Tag --> 4关联选择--> 4.4提取节点信息
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.aparents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])
