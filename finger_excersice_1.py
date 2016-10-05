# input() treats the typed line as a python expression and infers type.
# If we use raw_input() the input line is treated as a string. (python 2.7)

# in Python 3 only input() exist
a= [int(x) for x in input().split()]
bigSoFar = 0

for i in range (0,len(a)):
    if (a[i] % 2 !=0) :
        if (a[i] > bigSoFar):
            bigSoFar = a[i]

if (bigSoFar ==0):
    print("There are no odd number in the list")
print(bigSoFar)
