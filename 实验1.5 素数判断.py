a=int(input("输入:"))
for i in range(2,a):
    if(a%i==0):
        print("不是素数")
        break
else:
    print("是素数")
