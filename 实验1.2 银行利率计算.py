money=int(input("钱:"))
year=int(input("期限:"))
if(0<year<=1):
    money*=((1+0.0033)**(year*12))
elif(1<year<=2):
    money*=(1+0.0036)**(year*12)
elif(2<year<=3):
    money*=(1+0.0039)**(year*12)
elif(3<year<=5):
    money*=(1+0.0045)**(year*12)
elif(5<year<=8):
    money*=(1+0.0054)**(year*12)
else:
    print("请输入正确的年份")
print(money)