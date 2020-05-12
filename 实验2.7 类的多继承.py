class student:
    sid=0
    class_=""
    def study(self):
        print("My student's id is {}".format(self.sid))
        print("I major in {}".format(self.class_))

class teacher:
    tid=0
    dept=""
    def teach(self):
        print("And my teacher's id is{}".format(self.tid))
        print("I am in {}".format(self.dept))

class doctor(student,teacher):
    name=""
    age=0
    def __init__(self,sid,class_,tid,dept,name,age):
        self.sid=sid
        self.class_=class_
        self.tid=tid
        self.dept=dept
        self.name=name
        self.age=age
    def introduce(self):
        print("My name is {},I am {} years old".format(self.name,self.age))
        self.study()
        self.teach()

if __name__ == "__main__":
    doctor1=doctor(2013200,"Agricultural machinery engineering",20193066,"college of informatics","wpf",34)
    doctor1.introduce()