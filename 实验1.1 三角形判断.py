a=int(input("输入第一条边"))
b=int(input("输入第二条边"))
c=int(input("输入第三条边"))
d=0
if(a>=b+c or c>=b+a or b>=a+c):
    print("不能组成三角形")
else:
    if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2):
        print("直角三角形")
        d=1
    if((a==b and b!=c) or(a==c and a!=b) or(c==b and a!=c)):
        print("等腰三角形")
        d=1
    if(a==b and b==c):
        print("等边三角形")
        d=1
    if(d==0):
        print("普通三角形")
