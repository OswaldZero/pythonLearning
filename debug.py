import pdb
#pdb.run()
pdb.run("""
for i in range(0,10,3):
    i+=2
    print(i)
""")

#pdb.runeval()
pdb.runeval('(3+5)*2-6')

#pdb.runcall()
def sum(*args):
    s=0
    for x in args:
        s+=x
    return s
pdb.runcall(sum,2,4,6,8)

#pdb.set_trace()
pdb.set_trace()
for i in range(6):
    i*=i
    print(i)