import cmath
a=int(input("enter the value a"))
b=int(input("enter the value b"))
c=int(input("enter the value c"))
d=cmath.sqrt (b*b-4*a*c)
sol1=(-b+d)/(2*a)
sol2=(-b-d)/(2*a)
print(sol1)
print(sol2)
