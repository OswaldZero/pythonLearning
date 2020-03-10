import random
#1 if语句
#1.1 判断字符类型
i=input("input a char: ")
if(i.isdigit()):
    print("数字")
elif(i.isalpha()):
    print("字符")
else:
    print("其他")

#1.2 判断成绩
i=int(input("input the score: "))
if (i>=90 and i<=100):
    print("A")
elif (i<90 and i>=80):
    print("B")
elif (i<80 and i>=70):
    print("C")
elif (i<70 and i>=60):
    print("D")
elif (i>=0 and i<60):
    print("E")
else:
    print("error")

#1.3 判断闰年
i=int(input("input the year: "))
if ((i%4==0 and i%100!=0) or i%400==0):
    print("leap year")
else:
    print("not leap year")

#2 for语句
#2.1 遍历字符串
s1=input("输入字符串: ")
s2=""
for i in s1:
    s2+=i*3
print(s2)
lang=("C/C++","Java","Python")
for i in lang:
    print(i)

#2.2 遍历元组
tuple1=(1,2,3,4,5)
for i in tuple1:
    print(i)

#2.3 遍历列表
school=["动科院","植科院","生科院","食科院","理学院","信息学院"]
print(school)
print(len(school))
print(range(len(school)))
for i in range(len(school)):
    school[i]=school[i][0:2]
print(school)

#2.4 遍历字典
months={"jan":1,"feb":2,"mar":3}
for key in months:
    print(key)
for value in months.values():
    print(value)
for (key,value) in months.items():
    print((key,value))

#2.5 遍历文本行
firstChar=input("请输入首字母:")
file1=open("D:/home/test/wyh.txt")
for i in file1:
    if (i.startswith(firstChar)):
        print(i.rstrip())
file1.close()

#3 while 语句
#3.1 循环嵌套输出20-50之间的素数
for i in range(20,51):
    for j in range (2,int((i/2))+1):
        if (i%j==0):
            break
    else:
        print(i)   

#3.2 一维数组及其操作

i=int(input("请输入一维数组的个数: "))
sum1=0
list1=[random.randint(10,99) for j in range(i)]
for j in range(i):
    print(list1[j],end=" ")
    sum1+=list1[j]
print()
max1=max(list1)
min1=min(list1)
average1=float(sum1/i)
print("最大值: {0},最小值: {1},平均值: {2}".format(max1,min1,average1))

#3.3 二维数组及其操作
han=int(input("请输入行数: "))
lie=int(input("请输入列数: "))
list2=[[random.randint(10,99) for j in range(lie)] for i in range(han)]
max2=list2[0][0]
min2=list2[0][0]
sum2=0
for i in range(han):
    for j in range(lie):
        sum2+=list2[i][j]
        if (max2<=list2[i][j]):
            max2=list2[i][j]
        if (min2>=list2[i][j]):
            min2=list2[i][j]
        print(list2[i][j],end="  ")
    print()
average2=float(sum2/(han*lie))
print("最大值: {0},最小值: {1},平均值: {2}".format(max2,min2,average2))