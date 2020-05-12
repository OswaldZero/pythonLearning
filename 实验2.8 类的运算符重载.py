import math
class Vector3:
    x=0
    y=0
    z=0
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,anotherPoint):
        vector=Vector3(self.x+anotherPoint.x,self.y+anotherPoint.y,self.z+anotherPoint.z)
        return vector
    def __sub__(self,anotherPoint):
        vector=Vector3(self.x-anotherPoint.x,self.y-anotherPoint.y,self.z-anotherPoint.z)
        return vector
    def __mul__(self,n):
        vector=Vector3(self.x*n,self.y*n,self.z*n)
        return vector
    def __truediv__(self,n):
        vector=Vector3(self.x/n,self.y/n,self.z/n)
        return vector
    def __str__(self):
        s1="Vector"+"("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
        return s1
    def length(self):
        n=self.x**2+self.y**2+self.z**2
        return math.sqrt(n)
if __name__ == "__main__":
    v1=Vector3(3,4,5)
    v2=Vector3(5,6,7)
    print(v1+v2)
    print(v1-v2)
    print(v1*3)
    print(v2/2)
    print(v1.length())