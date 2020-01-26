class Encapsulation:
    def __init__(self):
        self.__age=64 # this is a global variable
    def sell(self):
        print("my amount is",self.__age)
    def setAge(age,ega):
        age.__age=ega
c=Encapsulation()

c.sell()

c.__age=46
c.sell()
c.setAge(46)
print(c.__age)
c.sell()
