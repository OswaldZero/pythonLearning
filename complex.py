class complex:
    def __init__(self,real,image):
        self.real=real; self.image=image
if __name__ == "__main__":
    t=complex(2.4,-4.6)
    x="("+str(t.real)+str(t.image)+")"; print(x)
    y=2.4+4.6j; print(y)