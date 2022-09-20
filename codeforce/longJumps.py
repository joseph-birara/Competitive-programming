t = int(input())
for k in range(t):
    
    n = int(input())
    a = list(map(int , input().split()))
    score = 0
    for ind in range(1,n+1):
        tot = 0
    
        while ind < n+1:
            tot += a[ind-1]
            ind +=a[ind-1]
        score = max(score,tot)
    print(score)
        
    
