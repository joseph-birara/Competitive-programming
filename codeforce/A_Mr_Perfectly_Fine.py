

testcase = int(input())

for _ in range(testcase):
    n = int(input())
    arr = []

    for j in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)

    first = float('inf')
    second = float('inf')
    both = float('inf')
    for m, b in arr:
        if b == 0:
            continue
        elif b == 11:
            both = min(m, both)
        elif b == 10:
            second = min(m, second)
        elif b == 1:
            first = min(m, first)
    var = min(both, second+first)

    if (first == float('inf') or second == float('inf')) and both == float('inf'):
        print("-1")
    else:
        print(var)
