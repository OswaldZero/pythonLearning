class Site:
    def __init__(self,name,url):
        self.name=name; self.__url=url
    def printme(self):
        print('name:',self.name)
        print('url:',self.__url)
    def __printme(self):
        print("1")
    def _printme(self):
        self.__printme()
        print("2")
if __name__ == "__main__":
    s=Site("hazu","www.hzau.edu.cn")
    s.printme()
    s._printme()
    #s.__printme()    