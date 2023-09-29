for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 'YES'
    increasing_started = 0
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            increasing_started = 1
        elif arr[i] > arr[i + 1] and increasing_started == 1:
            result = 'NO'
    print(result)
