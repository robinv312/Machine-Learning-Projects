import function
import datetime
import platform
import json
import re
x=platform.system()
print(x)
function.my_function(9)
t=dir(platform)

print(datetime.datetime.now())

io='{"name":"robin","age":"24"}'
oi=json.loads(io)
print(oi)
var= "my life is dedicated to god"
h=re.findall("ibbs",var)
if(h):
    print("a match is found")
else:
    print("sorry a match could not found")
print(re.split("\s",var))

try:
    y=5/0
except:
    print("exception has occured")
else:
    print("you are in the else part")
finally:
    print("you have covered almost all the cases")
