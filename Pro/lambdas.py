x=lambda a,b,k: (a*b)+k
print(x(3,6,5))

def myFunction(n):
    return lambda a:a*n
p=myFunction(2) #lambda a:a*2

print(p(11))
car=["my","love ","is","god"] #this is a list
print(car[2])
car.remove("my")
print(car)
car.append("always")
print(car)
for x in car:
    print(x)
s=len(car)
print(s)
cars=("x","y","z")
iterators=iter(cars)
print(next(iterators)+"  success")
