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
#一标签选择器Tag --> 4关联选择--> 4.2父节点和祖先节点
print( soup.a.parent)
# (1)获取节点的父节点parent属性
print(type(soup.a.parents))# (2) 获取节点的所有父节点parents 属性
print(list (enumerate(soup.a.parents)))
