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
#一标签选择器Tag --> 4关联选择--> 4.3 兄弟节点
print( 'next Sibling',soup.a.next_sibling) # (1)获取节点下一个节点
print( 'prev Sibling',soup.a.previous_sibling)# (2) 获取节点上一个节点
print( 'next Siblings',list(enumerate(soup.a.next_siblings))) # (1) 获取节点所有下一个节点
print( 'prev Siblings',list(enumerate(soup.a.previous_siblings)))# (2) 获取节点所有上一个节点
