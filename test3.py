testCases = int(input())
for test in range(testCases):
    n, m = map(int,input().split())
    arr = []
    for index in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    
