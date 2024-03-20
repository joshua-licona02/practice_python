from collections import Counter

def countingValleys(steps, path):
    level=0
    valley=0

    for step in path:
        if step == "U":
            level+=1

            if level == 0:
                valley+= 1
        else:
            level -=1
    return valley

print(countingValleys(input(), input())) 