def rotatedDigits(n):

    count = 0

    for i in range(1,n+1):
        num = str(i)

        print(num)

        if '3' in num or '7' in num or '4' in num:
            continue
        if '2' in num or '5' in num or '6' in num or '9' in num:
            count+=1
        
    return count

print(rotatedDigits(10))