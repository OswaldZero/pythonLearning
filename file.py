import os
import shutil
import csv
import xlrd
import xlwt
import xlutils.copy
import xml.etree.ElementTree as et
#txt文件操作: 打开、读取、创建、写入、关闭、定位、截断、复制、删除、重命名
f=open("wyh.txt","a+")
f.seek(0)
print(f.read(4))
f.seek(0)
print(f.readline())
f.seek(0)
print(f.readlines())

f.seek(0,os.SEEK_END)
f.write("\nwyh\n")
f.writelines(["wuhj\n","fsadf\n"])

f.seek(2,os.SEEK_SET)
print(f.tell())

f.seek(0,os.SEEK_SET)
print(f.truncate(12))
print(f.readlines())

os.chdir("D:/home/")

shutil.copy("D:/home/test/i.txt","D:/home/test1/i1.txt")
os.rename("D:/home/test/i.txt","i2.txt")
os.remove("i2.txt")

#dir目录操作：获取、创建、删除
print(os.getcwd())
print(os.listdir("D:/home/test1/"))

os.mkdir("D:/home/test3")
os.rmdir("D:\home\test3")

shutil.rmtree("D:/home/test2")

#csv文件操作：读、写
cr=csv.reader(open("test.csv",encoding="utf-8"))
for r in cr:
    print(r)

out=open("test.csv","w",newline="")
cw=csv.writer(out,dialect='excel')
cw.writerow(['1','2','3','4'])
out.close()


#xls文件操作：读、写、修改
book=xlrd.open_workbook("D:/home/test/wyh.xlsx")
n=book.nsheets
print(n)
list1=book.sheets()
print(list1)
sheet1=book.sheet_by_name("Sheet1")
print(sheet1.name)
print(sheet1.nrows)
print(sheet1.ncols)
print(sheet1.cell(1,1))
print(sheet1.cell_value(1,1))
print(sheet1.cell(1,1).value)

wb=xlwt.Workbook(encoding="utf-8")
sheet_1=wb.add_sheet("sheet1",cell_overwrite_ok=True)
sheet_1.write(0,0,"hzau")
sheet_1.row(0).write(1,"and")
sheet_1.write(0,2,"wpf")
sheet_1.col(2).width=300
wb.save('D:/home/test.xlsx')

book=xlrd.open_workbook("test.xlsx",formatting_info=True)
wtbook=xlutils.copy.copy(book)
wtsheet=wtbook.get_sheet(0)
wtsheet.write(0,0,'abc')
wtsheet.write(0,1,'wyh')
wtsheet.write(0,2,"123")
wtbook.save("test.xlsx")

#xml文件操作：解析、修改、创建

t=et.ElementTree(file="test.xml")
root=t.getroot()
print(root.tag,root.attrib)
for child in root:
    print(child.tag,child.attrib,end="  ")
print("\n",root[0].tag,root[0].text)
print(root[3][0].tag,root[3][0].text)

t=et.ElementTree(file='test.xml')
root=t.getroot()
del root[2]
root[0].set("university","hzau")
for child in root:
    print(child.tag,child.attrib,end=" ")
t.write("text.xml")

root=et.ElementTree("coi")
a=et.ElementTree("dean")
a.text="wyh"
b=et.Element("major")
b1=et.SubElement(b,"cs")
b1.text="wsl"
et.extend((a,b))
tree=et.ElementTree(root)
tree.write("new.xml")
