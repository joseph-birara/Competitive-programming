testCases= int(input())
for _ in range(testCases):
    n , m = map(int,input().split())
    k,h = map(int,input().split())

    if  (n == k) and (h+m ==k):
        print("YES")
    elif (k == m) and ( h+n ==k):
        print("YES")
    elif (h == m) and ( n+k ==m):
        print("YES")
    elif (h == n) and ( k+m ==h):
        print("YES")
    
    else:
        print("NO")
