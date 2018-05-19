dict1 = {'name': 'Anand', 'addr': 'Bangalore', 'age': 26}
print (dict1)

dict2 = dict([('name', 'Anand'), ('addr', 'bangalore'), ('age', 21)])
print (dict2)

dict3 = dict(name='Anand', addr='bangalore', age=24)
print (dict3)

# baisc dict operation

dict2['addr'] = 'Bangalore'
print (dict2)

print (len(dict2))

print ('addr' in dict2)  # looks for key

print ('addr' not in dict2)

dict3.clear()
print (dict3)

del dict3

# accessing key & values in dict
print (dict1.keys())
print (dict1.values())
print (dict1.items())
a, b, c = dict1.items()
print (a, b, c)
print ('Anand' in dict1.values())

# iterating a dict

for item in dict1:
    print (item, dict1[item])

for key, val in dict1.items():
    print ((key, val))
