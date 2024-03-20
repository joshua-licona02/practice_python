def myFunction(n,m):
    return n*m

print(myFunction(3,4))

# Nested functions
def outer(a,b):
    c = "c"

    def inner():
        return a + b + c
    return inner()
print(outer("a", "b"))


def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i]*=2

        nonlocal val
        val *=2
    helper()
    print(arr, val)
nums = [1,2]
val = 3

double(nums, val)