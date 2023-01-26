testCases = int(input())
for _ in range(testCases):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    result = 0
    left = 0
    for right in range(1,n):
        
        if arr[right-1] >=2*arr[right] :
            left = right
        elif right-left == k:
            result +=1
            left+=1
       
            

    print(result)

          

        
       

        

            



