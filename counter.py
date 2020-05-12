class Counter:
    __priCount=1
    pubCount=1
    def count(self):
        self.__priCount+=1
        self.pubCount+=2
        print(self.__priCount)


if if __name__ == "__main__":
    c1=Counter()
    c1.count()
    print(c1.pubCount)
    #print(c1.__pubCount)