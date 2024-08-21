mydict = {}
newdict =  dict()
print(type(mydict))

mydict['a'] = 1
mydict['b'] = 1
mydict['c'] = 1
mydict['d'] = 1
mydict['e'] = 1
mydict['f'] = 1

print(mydict)

#creates a dictory with the keys
print(mydict.fromkeys([4,5]))

newdict = newdict.fromkeys([4,5], 0)
print(newdict)

print(mydict)

#get the value from the key
print(mydict.get('d'))

#returns key and value like this dict_items([('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1)])
print(mydict.items())

print(mydict.keys())

print(mydict.pop('d'))
print(mydict)