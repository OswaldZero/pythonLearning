class myClass:
    """
    example
    """
    i=12
    def fun(self):
        return "hello python"
if __name__ == "__main__":
    myclass=myClass()
    print(myclass.i)
    print(myclass.fun())
    myclass.i=56
    print(myclass.i)