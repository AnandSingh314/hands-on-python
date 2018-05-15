#constructor - creating new sets
set1 = {}  # incorrect way of creating sets
set2 = {11, 45, 32, 23, 32, 23, 45, 11}
set3 = set()
set4 = set([11, 45, 32, 23, 32, 23, 45, 11])

print set1
print set2
print set3
print set4

# set comprehension
set5 = {x % 5 for x in range(15) if x > 2}
print set5

# add
set6 = {32, 11, 45, 23}
set6.add(100)
set6.add(200)
print set6

# remove
set6.remove(100)
print set6

# len
print 'len of set6:', len(set6)

# in, not in
print 100 in set6
print 100 not in set6

# pop
set6.pop()
print set6

# clear
set6.clear()
print set6

# Mathematical Operation
setA = {'Red', 'Blue', 'Green', 'Yellow', 'Brown'}
setB = {'Brown', 'Voilet', 'Purple', 'Blue', 'Green'}
print 'setA:', setA, '\n', 'setB:', setB

# Intersection
print 'setA & setB:', setA & setB

# Union
print 'setA | setB:', setA | setB

# Symmetric Difference
print 'setA ^ setB:', setA ^ setB

# Difference
print 'setA - setB:', setA - setB

# Subset
print 'setA <= setB:', setA <= setB
print 'setA <= setB:', {'Blue', 'Brown'} <= setA

# Superset
print 'setA >= setB:', setA >= setB
print 'setA >= setB:', setA >= {'Blue', 'Brown'}

