# find the cube root of a perfect cube

x = int(input())
ans = 0

# while the answer to the cube is less than the absolute value of the input we increment answer by 1
while (ans**3 < abs(x)) :
    ans = ans+1
# the answer is exactly equal to the input or is more.
#If is not equal we conclude that the input is not a perfect cube
if (ans**3 != abs(x)):
    print (x, " Is not a perfect cube")
else:
    if (x < 0):
        ans = -ans
    print ("Cube root of " + str(x) + " is " + str(ans))