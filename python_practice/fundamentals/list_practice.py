fruits = ["apple", "banana", "peach"]

y = fruits[1] #index

print(y) #prints banana

print(fruits)

print(len(fruits))

mix = [1,4,"name", True, "abc"]

print(mix)
print(type(mix[2]))
print(type(mix[3]))

newlist = list(("a","b","c"))
print(newlist)

fruits[1:2] = ["kiwi","watermelon"]
print(fruits)

fruits.insert(3, "fruity")
print(fruits)

fruits.append("orange")
print(fruits)

addons = ["bmw", "volvo", "tesla"]

fruits.extend(addons)
print(fruits)


for i in range(len(fruits)):
    print(fruits[i])

for i, n in enumerate(fruits):
    print(i,n)

nums1 = [1,3,5]
nums2 = [2,4,6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
    
#input size of list
# n = int(input("Input size of list: "))

# lst = list(map(int, input("Enter the integers: ").strip().split()))[:n]
# print("List",lst)

print(fruits)

fruits.sort(key = lambda x: len(x)) #Sort by length of string
print(fruits)

#create 2-d array
array = [[0]*4 for i in range(4)]
print(array)