l=[]
while True:
	s=input("enter the values")
	if len(s)>=12:
		break
	l.append(tuple(s.split(",")))
print(sorted(l,key=itemgetter(0,1,2)))