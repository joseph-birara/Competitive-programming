def is_possible(k, arr):
    n = len(arr)
    res = k
    for i in range(1, n):
        res += min(k, arr[i] - arr[i-1])
    return res


tests = int(input())
for _ in range(tests):
    n, h = map(int, input().split())
    seconds = list(map(int, input().split()))

    low = 1
    high = h
    flag = 0
    temp = h

    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid, seconds) > h:
            high = mid-1
        elif is_possible(mid, seconds) < h:
            low = mid+1
        elif is_possible(mid, seconds) == h:
            print(mid)
            flag = 1
            break
    if not flag:
        print(low)
