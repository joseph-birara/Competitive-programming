testCases = int(input())

for _ in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 0
    for j in range(1, n):
        if arr[j] - arr[j-1] > 1:
            res += 1
    if res > 0:
        print("NO")
    else:
        print("YES")
