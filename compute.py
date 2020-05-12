class Compute:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value+other.value
    def __sub__(self,other):
        return self.value-other.value
if __name__ == "__main__":
    c1=Compute(20); c2=Compute(10)
    print(c1+c2)
    print(c1-c2)