import os
f=open("demofile.txt","r")
print(f.readline())
print(f.readline())
for x in f:
    print(x)
#write operation
f=open("demofile.txt","a")
f.write("hai all i will propage this message to the entire world")
d=open("demofile.txt","r")
print(d.read())

#create a new file
g=open("robinSampleFile.py","x")
#to delete the files that are created

os.remove("robinSampleFile.ods")
