list1 = list()
list2 = ['a', 25, 'string', 14.03]
# list3 = list(tupel1)

print list1
print list2

# List Comprehension
list4 = [x for x in range(10)]
print list4
list5 = [x**2 for x in range(10) if x > 4]
print list5

# del(): delete list item or list itself
list6 = ['sugar', 'rice', 'tea', 'cup']
del (list6[1])
print list6
# below line will delete the list
del (list6)

list7 = ['sugar', 'tea', 'cup']
list7.append('ginger')
print list7

# extend(): add 2 list together
list8 = ['coffee', 'crush']
list7.extend(list8)
# list7 += list8
print list7
print list8

# insert(): inster item at given index and push rest forward
list9 = [5, 3, 7, 4, 9]
list9.insert(0, 100)
list9.insert(len(list9), 999)
print list9
list9.insert(1, ['One', 'Two'])
print list9

# pop(): pop the top item from list
list10 = [5, 3, 7, 4, 9]
list10.pop()
list10.pop()
print list10

# remove(): only remove 1st occurance of item
list11 = [5, 3, 7, 4, 9, 3, 7]
list11.remove(3)
print list11

# reverse(): reverse the list item
list12 = [5, 3, 7, 4, 9, ]
list12.reverse()
print list12

# sort(): sort the list item, unlike sorted() this will sort the existing list.
list13 = [5, 3, 7, 4, 9, ]
list13.sort()
print list13

