#colours =  {"Red" : 198, "Green" : 170, "Blue" : 160}
#for key, value in colours.items():
    #print(key, value)
from collections import OrderedDict
#animal=namedtuple('animal','name age size')
#perk=animal(name="cat",age=56,size=56)
#print(perk.name)
#colours = (
    #('Yasoob', 'Yellow'),
    #('Ali', 'Blue'),
    #('Arham', 'Green'),
    #('Ali', 'Black'),
    #('Yasoob', 'Red'),
    #('Ahmed', 'Silver'),
#)

#favs = Counter(x for x, colour in colours)
#print(favs)

#from collections import OrderedDict

#colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
#for key, value in colours.items():
#    print(key, value)
import pdb

def make_bread():
    print(dir(pdb))
    #pdb.set_trace()# for he debugging purpose
    return "I don't have time"

print(make_bread())
