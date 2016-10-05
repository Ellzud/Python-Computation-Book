x = int(input("please enter a positive integer : " ))
root = 0
power = 0



for r in range(1,x):        #root from 1 to x-1
    for p in range(1,7):    #power from 1 to 6
        if(r**p == x):      #if an answer is found break from the inner loop
            root = r
            power = p
            break
    if(root**power == x):
        print ("answer found " + str(root) + " " + str(power))
        break
if (root**power != x):
    print("No answer was found in the form of root^power")