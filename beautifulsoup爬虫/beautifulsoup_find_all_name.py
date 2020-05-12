html="""
    <div class="pane1">
        <div class="panel-heading">
            <h4>He11o</h4>
        </div> 
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</l1>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-smal1" id= "list-2">
                <1i class="element">Foo</li>
                <1i class="element">Bar</li> 
            </ul>
        </div> 
    </div> 
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup (html,'lxml')
#方法选择器
#1find_all()查询所有符合条件的元素，传入一些属性
#或文本来得到符合条件的元素，功能十分强大
print(soup.find_all(name='ul')) # (1) name 参数
print(type(soup.find_all(name='ul')[0]) )
for ul in soup.find_all(name='ul'):#查询出所有u1标签后
    print(ul.find_all(name='1i')) # 再继续查询其内部的1i标签
for li in ul.find_all(name='li') :
    print(li.string)#遍历每个1i获取其文本
