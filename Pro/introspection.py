import itertools
from pprint import pprint
my_list=[[1,2,2,2,3,3,4],[3,4,5],[4,9,0]]
pprint(list(itertools.chain.from_iterable(my_list)))
print(type(my_list))
