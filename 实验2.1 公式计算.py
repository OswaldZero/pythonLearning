

def sum_(n):

    def fz(n):
        if(n==1):
            return 1
        else:
            return n+fz(n-1)

    def fm(n):
        if(n==1):
            return 1
        else:
            return n*fm(n-1)

    sum1=0.0

    for i in range(1,n+1):
        sum1+=(fz(i)/fm(i))
    return sum


