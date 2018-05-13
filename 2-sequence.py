x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Slicing works like [start:end+1:step]

print 'x:', x
print 'length of x:', len(x)
print 'at 0 index:', x[0]
print 'at 3rd index:', x[3]
print 'reverse indexing -1, -2, -3:', x[-1], x[-2], x[-3]

print 'slicing from:', x[1:4]
print 'slicing with step 2:', x[1:10:2]
print 'from index 5 to end:', x[5:]
print 'from last 5 to end:', x[-5:]
print 'from start to index 5:', x[:5]
print 'all except last 10:', x[:-10]

# adding/concatenating 2 or more sequence only same type
print 'anand' + 'vijay' + 'singh'
# multiplying sequence like string or list
print 'bug' * 2
list1 = [2, 3] * 3
print list1

# checking membership
print 5 in [1, 2, 3, 4, 5, 6]
print 'A' in x
print '5' in [1, 2, 3, 4, 5, 6]
print 'cow' not in ['fox', 'ox', 'cow']

print 'iterating thru item in a sequnce'
seq = [8, 3, 5]
# item
for item in seq:
    print 'double of item:', item * 2
    print 'square of item:', item**2

# item and index
for index, value in enumerate(seq):
    print 'index:', index, 'value:', value

# number of items in sequence
print 'length of:', len(['a', 'z', 'c', 'y'])
print 'length of:', len([11, 22, 33, 44, 55])
print 'length of string:', len('string')

# min and max of items in sequence
print 'min, max of:', min(['az', 'za', 'c', 'y']), max(['az', 'za', 'c', 'y'])
print 'min, max of:', min([11, 22, 33, 44, 55]), max([11, 22, 33, 44, 55])
print 'min, max of string:', min('string'), max('string')

# sum of list, all item must be numeric type
intlist = [22, 33, 11, 44, 55]
print 'sum of list:', sum(intlist)
# print 'mix match data type sum will error: ', sum([1,'2',3,'4',5,'6'])
print 'sum of last 2 item in list:', sum(intlist[-2:])

#sorting
# returns new sorted list without modifying existing list
string = 'string'
print sorted(string)
print sorted(['pig', 'cow', 'horse'])

# counting items in sequence
cntstr = 'hippo'
print cntstr.count('p')
print ['pig', 'cow', 'cow', 'cow', 'horse'].count('cow')

# index() return first occurance of item exist in sequence
print cntstr.index('p')
print ['pig', 'cow', 'cow', 'cow', 'horse'].index('cow')

# unpacking, assigning all items in sequence
x = ['pig', 'cow', 'horse']
a, b, c = x
print a, b, c
