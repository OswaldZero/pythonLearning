class person:
    name=""
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("my name is {},I am {} years old".format(self.name,self.age))

class teacher(person):
    profession=""
    title=""
    course=""
    def __init__(self,name,age,profession,title,course):
        self.name=name
        self.age=age
        self.profession=profession
        self.title=title
        self.course=course
        

    def speak(self):
        print("my name is {},I am {} years old".format(self.name,self.age))
        print("my profession is {}".format(self.profession))
        print("my title is {}".format(self.title))
        print("my master course is {}".format(self.course))

if __name__ == "__main__":
    teacher1=teacher("wpf",42,"computer","teacher","python")
    teacher1.speak()