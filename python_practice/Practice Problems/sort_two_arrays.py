def sort_and_merge(arr1, arr2):

    arr1.extend(arr2)
    arr1.sort()

    return arr1
    # if arr1[-1] < arr2[0]:
    #      arr1.extend(arr2)
    #      return arr1
    # else:
    #     arr2.extend(arr1)
    #     return arr2

arr1 = [5,8,2,6,4]
arr2 = [1,9,3,7]

print(sort_and_merge(arr1,arr2))