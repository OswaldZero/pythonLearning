from people_student import student
class speaker:
    topic=""
    def __init__(self,t):
        self.topic=t
    def speak(self):
        print("I am a speaker,my topic is %s"%(self.topic))
class sample(speaker,student):
    def __init__(self,n,a,w,h,g,t):
        speaker.__init__(self,t)
        student.__init__(self,n,a,w,h,g)
    def speak(self):
        speaker.speak(self)
        student.speak(self)
if __name__ == "__main__":
    s=sample("wyh",18,65,170,9,"english")
    s.speak()