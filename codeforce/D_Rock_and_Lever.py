from collections import defaultdict


test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    d = defaultdict(int)

    for i in range(n):
        k = len(bin(arr[i]))
        d[k] += 1
        count += d[k]-1

    print(count)
