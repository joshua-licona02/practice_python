from collections import deque
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(4 in mySet)

mySet.remove(2)
print(mySet)

print(set([1,2,3,4,5]))
print(set)

loopSet = {i for i in range(7)}
print(loopSet)


# HashMap (dict)

myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice":90, "bob":70}
print(myMap)

#Dict comprehension
dictMap = {i: 2*i for i in range(3)}
print(dictMap)

#Looping through map
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)