def fac(n):
    if(n==1):
        return 1
    else:
        return n*fac(n-1)

def calculate(m,n):
    sum=fac(n)/(fac(m)*fac(n-m))
    return sum