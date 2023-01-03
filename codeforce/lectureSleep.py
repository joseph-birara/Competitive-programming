n,k = map(int,(input().split()))
result =0
theorems = list(map(int,input().split()))
t = list(map(int,input().split()))
for i in range(n):
    sum = 0
    m = k
    for d in range(n):
        if (m > 0 and n-k +1 >=0 and d>=i) or t[d] ==1:
            sum += theorems[d]
            if d >=i and m >=0:
                m -=1
    result = max(result,sum)
print(result)


