import collections

print ('Regular dictionary:')
d = {}
d['a'] = 'A'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
d['b'] = 'B'

print(d)

print ('\nOrderedDict:')
d2 = collections.OrderedDict()
d2['a'] = 'A'
d2['b'] = 'B'
d2['d'] = 'D'
d2['e'] = 'E'
d2['c'] = 'C'

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'
print(d2)
print(d2==d1)
