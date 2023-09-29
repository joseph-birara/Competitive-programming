testCases = int(input())

for _ in range(testCases):
    n = int(input())
    weight = list(map(int, input().split()))
    reversed_w = weight[:]

    for i in range(1, n):
        weight[i] += weight[i-1]
    for i in range(n-2, -1, -1):
        reversed_w[i] += reversed_w[i+1]

    max_caney = 0
    left = 0
    right = n-1

    while left < right:
        if weight[left] == reversed_w[right]:
            max_caney = left + 1 + n-right
            left += 1
            right -= 1
        elif weight[left] > reversed_w[right]:
            right -= 1
        else:
            left += 1

    print(max_caney)
