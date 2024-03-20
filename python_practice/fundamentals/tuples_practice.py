# Tuples are like arrays but immutable

tup = (1,2,3)
print(tup)

myMap = {(1,2):3}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)