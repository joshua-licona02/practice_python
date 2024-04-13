def uniqueOccurrences(arr):

    dict = {}

    for nums in arr:
        if nums in dict:
            dict[nums] +=1
        else:
            dict[nums]=1

    occurrence = list(dict.values())
    return len(occurrence) == len(set(occurrence))

arr = [1,2,2,1,1,3]
arr1 = [1,2]

print(uniqueOccurrences(arr1))