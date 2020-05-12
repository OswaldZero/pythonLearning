a=int(input("Chinese:"))
b=int(input("Endlish:"))
c=int(input("Math:"))
d=int(input("PE:"))
if((a+b+c+d<330) or a<60 or b<60 or c<60 or d<60):
    print("没有录取")
elif((a+b+c+d<=380)):
    print("自费")
else:
    print("公费")