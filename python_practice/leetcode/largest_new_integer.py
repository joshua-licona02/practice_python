def largestGoodInteger(num):

    
    for digits in num:

        if int(num[digits])==int(num[digits+1]):
            return digits
        else:
            return False


num = "2300019"
largestGoodInteger(num)