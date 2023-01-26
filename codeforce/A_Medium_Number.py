testCases = int(input())
for _ in range(testCases):
    arr = list(map(int,input().split()))
    arr.sort()
    print(arr[1])

