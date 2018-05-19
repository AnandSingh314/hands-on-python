tuple1 = ()  # no-item tuple
tuple2 = (1, 2, 3, 4)
tuple3 = 1, 2, 3, 4  # parenthesis are optional
tuple4 = 3,  # single item tuple
tuple5 = tuple(['one', 'two', 'three', 'four'])  # tuple from list

print (tuple1)
print (tuple2)
print (tuple3)
print (tuple4)
print (tuple5)

# tuple is immutable, below line show error while modification.
# del(tuple3[1])
# tuple3[2]=10

tuple6 = ([1,2,3,],10)
tuple6[0][1]=20
print (tuple6)
del(tuple6[0][1])
print (tuple6)

tuple7 = 1,2,3,4,5,6,7,8,9
print (3 in tuple7)
print (3 not in tuple7)