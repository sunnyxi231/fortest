
from array import array
from pprint import pprint
#str = "0000000this is string example....wow!!! OMG COOL  1 23 3"
#b = str.split()
#print (str.split('i',2))
b = array('d',[1,2,3,4])
print(b)
print(b.typecode)
b.append(3)
pprint(b)