is_nice = True
state = "nice" if is_nice else "not nice"
print(state)
obj=[x for x in range(100) if x%2==0 if x%5==0]
print(obj)
we=["even" if x%2==0 else "odd" for x in range(100)]
print(we)
