def avg(marks):
    assert len(marks)!=0,"list is empty"
    return sum(marks)/len(marks)
marks1=[5,6,2]
print("average of marks",avg(marks1))
