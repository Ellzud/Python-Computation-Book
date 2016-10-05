
a= [int(x) for x in input().split()]
bigSoFar = 0

for i in range (0,len(a)):
    if (a[i] % 2 !=0) :
        if (a[i] > bigSoFar):
            bigSoFar = a[i]

print(bigSoFar)
