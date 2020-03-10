'''
@author 吴义虎
@date 2020/03/06
@email 1726036835@qq.com
'''
# 1 列表(list)
# 1.1 创建空列表
list1=[]
list2=[1]
list3=["wyh","hzau",2000,2020]
list4=[1,2,3,4,5,6,7,8]

# 1.2 截取,切片与更新
print("list3[1]:",list3[0])
print("list3[1:5]:",list3[1:5])
print(list3)
list3[3]=2001
print("list[3]:",list3[3])


# 1.3 内建方法
list3.append("fas")
list4.clear()
print(list4)
list5=list3.copy()
print(list5)
print(list3.count(2020))
list3.extend([1,2,4])
print(list3)
list3.index(2)
list3.insert(3,"fasdfsa")
print(list3.pop(3))
list3.remove(2)
list3.reverse()
print(list3)
list7=[6,5,8,2,5,1]
print(list7)
list7.sort()
print(list7)

# 1.4 内建函数
del list3[3]
len(list3)
max(list7)
min(list7)
list((1,2,34,54))

# 1.5 拼装与组合
print([1,2,3]+[4,5,6])
print(["wyh"*3])
print(3 in [1,2,3])
for i in [1,2,3,4]:
    print(i,end=" ")

# 1.6 嵌套
list3.clear()
list3=[[1,3,4],[1,4,5]]
print(list3[1][0])

# 2.元组(tuple)
# 2.1 创建
tuple1=("wyh","hzau",2000,2020)
print(tuple1)
tuple2=(1,2,3,4)
print(tuple2)
tuple3=()
tuple4=(3,)
print(tuple4)

# 2.2 访问
print(tuple2[1])
print(tuple2[-1])
print(tuple2[1:3])
print(tuple2[:-1])

# 2.3 修改不允许,但可以组合
tuple5=(1,23,4)
tuple6=tuple2+tuple5
print(tuple6)

# 2.5 删除
del tuple6

# 2.6 运算符
len((1,23,3))
(1,23,3)+(4,5,6)
("hi",)*4
3 in (1,3,4)
for i in (1,23,3):
    print(i,end=" ")
print("\n")
# 2.7 内建函数
len(tuple2)
max(tuple2)
min(tuple2)
tuple(list3)

# 2.8 内建方法
tuple2.index(2)

# 3.字典(dictionary)
# 字典的键必须唯一,且不可变
# 3.1 访问
dict1={"wyh":19,"cx":19,"wyb":8}
dict5={}
print(dict1)

# 3.2 内建函数
len(dict1)
print(str(dict1))
print(type(dict1))

# 3.3 内建方法
dict2={"wyh":19}
dict2.clear()
dict2=dict1.copy()
dict3=dict1.fromkeys(["q","w","e","r"])
print(dict3)
print(dict1.get("wyh",-1))
print(("wyh" in dict1))
print(dict1.items())
print(dict1.keys())
print(dict1.pop("wyh"))
print(dict1.popitem())
print(len(dict1))
#和get类似,只不过假如没找到就设置一个key,值为默认的
dict1.setdefault("wyh",19)
dict1.update({"wls":89})
print(dict1.values())

# 4.集合(set)
# 4.1 创建
set1=set("python1")
set2=frozenset("python2")
print(set1==set2)

# 4.2 访问
for i in set1:
    print(i,end=" ")
print("\n")

# 4.3 更新(只有可变集合可以更新)
set1.add("x")
set1.update("l")
set1.remove("x")

# 4.4 集合操作符与内建函数
set3=set1.copy()
set3.clear()
print(set1)
# 4.4.1差集
s6=set1-set2
print(set1.difference(set2))
set4={1,2,3}
set1.difference_update(set4)
print(set4,"\n",set1)
set1.discard("l")
# 4.4.2取交集
s1=set1&set4
s2=set1.intersection(set4)
# 4.4.3并集
s3=set1|set4
s4=set1.union()
# 4.4.4对称差分
s7=set1^set4
s8=set1.symmetric_difference(set4)
# 4.4.5 普通操作符
ste1=set("wyh")
ste2=set("wyhlif")
print(ste1<ste2)
print(ste1==ste2)
# 4.4.6 其他内建方法
#类似于discard,只不过这个有异常机制
set1.remove("p")
#删除任意一个且返回
set1.pop()
#清除所有元素
set1.clear()
