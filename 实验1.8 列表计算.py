import random
import math
list1=[random.randint(10,50) for i in range(10)]
print(list1)
print(max(list1))
print(min(list1))
sum=0
for i in list1:
    sum+=i
print(sum/10)