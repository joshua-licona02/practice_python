def numJewelsInStones(jewels, stones):

    count = 0

    for char in stones:
        if char in jewels:
            count +=1
    
    return count

jewels = "aA"
stones = "aAAbbbb"

print(numJewelsInStones(jewels, stones))