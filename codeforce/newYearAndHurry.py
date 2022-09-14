n, k = input().split()
n = int(n)
k = int(k)
count = 0
t = 240-k
 
 
for i in range(1,n+1):
    if t >= (i*5):
        count += 1
        t -= i*5
    else:
        break
print(count)