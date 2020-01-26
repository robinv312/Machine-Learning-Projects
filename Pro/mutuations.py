def add_to(num, target=[]):
    target.append(num)
    return target

e=add_to(1)
print(e)
# Output: [1]

e=add_to(2)
print(e)
# Output: [1, 2]

e=add_to(3)
print(e)
