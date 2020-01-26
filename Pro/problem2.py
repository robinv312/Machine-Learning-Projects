def PutNumbers(n):
	j=0
	while j<=n:
	   if j%7==0:
	     yield j
	   j=j+1
for x in PutNumbers(100):
	print(x)