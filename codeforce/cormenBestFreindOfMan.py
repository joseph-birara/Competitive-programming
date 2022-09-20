n ,k = map(int , input().split())
a = list(map(int , input().split()))
tot = 0
for i in range(1,n):
    x = a[i]
    if a[i] + a[i-1] < k:
        a[i] = k-a[i-1]
        tot += a[i] -x
print(tot)
print(' '.join(map(str, a)))
    
