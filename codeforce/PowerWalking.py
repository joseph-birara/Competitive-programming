t = int(input())
for _ in range(t):
    n = int(input())
    distinct = set(input().split())
    
    for i in range(1 , n+1):
        print(max(i , len(distinct)) , end=" ")
        
    print(end = "\n") 