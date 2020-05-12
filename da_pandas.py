from pandas import Series
from pandas import DataFrame
#1 Series对象创建与操作
list1=[1,2,3,4]
tuple1=(5,6,7,8)
dict1={"wyh":18,"ww":18}
ser1=Series(list1)
ser2=Series(tuple1,index=[3,1,2,4])
ser3=Series(dict1)
print(ser1,ser2,ser3)

#2 DataFrame对象创建与操作
obj={'name':['wyh','cx'],
     'age':['20','18'],
     'status':['student','student']}
df=DataFrame(obj)
df['gender']=['m','m']
del df['status']
print(df.head(),df.age,df.T)

