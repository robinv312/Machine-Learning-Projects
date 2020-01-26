class Parent:
    def __init__(self):
        print("hai welcome to the parent node")
    def buy():
        print("you are in the parent buy method")
class Child(Parent):
    def __init__(self):
      super().__init__()
    def buy(self):
        print("you are inside the buy method of child")
obj=Child()
obj.buy()
g= open("encapsulation.py",'x') 
