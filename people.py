class people:
    name=""
    age=0
    __weight=0
    __height=0
    def __init__(self,n,a,w,h):
        self.name=n
        self.age=a
        self.__weight=w
        self.__height=h
    def speak(self):
        print("{} is speaking:I am {} years old".format(self.name,self.age))
        print("my weight is {} kg,my height is {} cm".format(self.__weight,self.__height))
if __name__=="__main__":
    p=people("wyh",18,65,170)
    p.speak()
    