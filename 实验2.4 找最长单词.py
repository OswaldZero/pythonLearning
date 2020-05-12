def maxWord(s):
    list1=s.split(" ")
    j=len(list1[0])
    k=""
    for i in list1:
        if(len(i)>j):
            j=len(i)
            k=i
    return k