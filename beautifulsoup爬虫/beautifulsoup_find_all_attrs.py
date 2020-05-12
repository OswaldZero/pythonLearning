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
print(soup.find_all(attrs={"id":"list-1"}))
print(soup.find_all(attrs={'name':'elements'}))
print(soup.find_all(id='list-1'))