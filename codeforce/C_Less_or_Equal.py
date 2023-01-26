n,k = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()
arr.insert(0,1)
if k == n or arr[k+1] - arr[k]:
    print(arr[k])
else:
    print(-1)
        


    
