n,m = input().split()
n,m = int(n),int(m)
ans = 0
while m>n:
    if m%2 !=0:
        m +=1
    else:
        m /=2
    ans +=1
ans += n - m
print(int(ans))