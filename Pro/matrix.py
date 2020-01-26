import numpy as np
A=[[1,2,3],
   [2,4,6]]

print(A)
print(len(A)) # prints the number of rows in an array
print(type(A))
a=np.array([1,2,3],dtype=float)
print(a)
print(type(a))
zero_array=np.zeros((2,3))
print(zero_array)
zero_array=np.ones((2,3))
print(zero_array)
ara=np.arange(12).reshape(2,6)
print(ara.transpose())
print(ara[1,0])
#bra=np.arange(6)
#sum=ara.dot(bra)
print(ara)
f=np.datetime64('2005-02','D')
print(f)
