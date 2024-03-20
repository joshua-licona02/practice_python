a = "Hello world"

print(a[1])

print(a[2:5])   # llo
print(a[:5])    # Hello
print(a[2:])    # llo world
print(a[-5: -2]) # wor

b = "Joshua, Licona"

print(b.split(","))

quantity = 2
itemno = 69
price = 420

myorder = "I want {} pieces of item {} for {} dollars"

print(myorder.format(quantity, itemno, price))

strings = ["a","b","c"]
print(strings)
print("".join(strings))

print(a.split(" "))