for i in range(2,1001):
    b={1}
    c=0
    for j in range(2,i):
        if(i%j==0):
            b.add(j)
    for k in b:
        c+=k
    if(c==i):
        print(i)