year=int(input("year:"))
month=int(input("month:"))
leap=False
day=31
if((year%4==0 and year%100!=0) or year%400==0):
    leap=True
if(month in [1,3,5,7,8,10,12]):
    day=31
elif(month==2):
    if(leap):
        day=29
    else:
        day=28
else:
    day=30
print(day)