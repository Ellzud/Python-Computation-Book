# uses python3

fN = int(input())
f = [] 
f.append(0)
f.append(1)

for i in range(2,fN+1):
    f.append((f[i-1] + f[i-2]) % 10)

print(f[fN])