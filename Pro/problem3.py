from operator import itemgetter,attrgetter
student_tuple=[('Abin','A',12),('Cinu','B',23),('Aameeraa','y',45)]
d=sorted(student_tuple,key=itemgetter(0,1,2))
#Sf=sorted(student_tuple,key=attrgetter('name'))
print(d)
#print(f)