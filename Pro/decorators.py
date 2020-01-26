def A(func):
    def inner():            
        print ("i got decorated1")
        func()
        print("back")
    return inner
@A
def ordinary():
    print("iam ordinary2")
print("test")
ordinary()
print("vague")
#c=A(ordinary)
