def repeatedStrings(s, n):
    count = 0

    for i in range(0, len(s)):
        if s[i] == "a":
            count+=1
    count*=int(n / len(s))
    for i in range(0, n % len(s)):
        if s[i] == "a":
            count+=1
    return count

print(repeatedStrings(input(), input()))