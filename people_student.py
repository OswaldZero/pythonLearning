import people
class student(people.people):
    grade=""
    def __init__(self,n,a,w,h,g):
        super().__init__(n,a,w,h)
        self.grade=g
    def speak(self):
        super().speak()
        print("%s says: I am in grade %d"%(self.name,self.grade))
if __name__ == "__main__":
    s=student("wyh",18,65,170,9)
    s.speak()
