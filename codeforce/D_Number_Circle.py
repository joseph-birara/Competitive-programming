n = int(input())

arr = list(map(int,input().split()))

arr.sort(reverse=True)

if arr[2] +arr[1]> arr[0]:
    arr[0] , arr[1] = arr[1], arr[0]
    print("YES")
    print(*arr)
else:
    print("NO")

