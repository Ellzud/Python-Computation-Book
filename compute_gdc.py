# uses python3

n = [int(x) for x in input().split()]




def calculateGDC(a, b):
    currentA = -1
    currentB = -1
    remainder = -1
    if a == b:
        return a

    if a!=0 and b!=0 :
        if (a > b):
            currentA = a
            currentB = b
        else:
            currentA = b
            currentB = a
        while currentB != 0:
            remainder = currentA % currentB
            currentA = currentB
            currentB = remainder
        return currentA
        
    if a == 0:
        return b
    else:
        return a


gdc = calculateGDC(n[0], n[1])
print (gdc)

