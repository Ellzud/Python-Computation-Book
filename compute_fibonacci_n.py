# uses python3

fN = int(input())
f1 = 1
f2 = 1
fResult = 0

if (fN== 0):
    fResult=0
else:
    if (fN == 1 or fN == 2):
        fResult=1
    else:
        for i in range(3, fN+1):
            fResult = f1 + f2
            f1 = f2
            f2 = fResult
print(fResult)