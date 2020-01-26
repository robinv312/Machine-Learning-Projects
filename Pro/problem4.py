p=str(input("enter the string"))
t={'digits':0,'letters':0}
for c in p:
	if c.isdigit():
	 t['digits']+=1
	elif c.isalpha():
	 t['letters']+=1
	else: 
	  pass
print("letters",t['letters'])
print("digits",t['digits'])
