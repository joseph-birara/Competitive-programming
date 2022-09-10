n = int(input())
for _ in range(n):
    k = int(input())
    sque = list(map(int, input().split()))
    sque.sort()
    
    first , second = sque[0],0
    l, r= 1, k-1
    
    while l < r:
            first += sque[l]        
            second += sque[r]
            l +=1
            r -=1
    if second > first:
        print("YES")
    else:
        print('NO')
    
        
    