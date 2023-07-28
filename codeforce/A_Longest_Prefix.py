def longest_common_prefix(a, b):
    n = len(a)
    m = len(b)
    positions = {}

    for i in range(m):
        if b[i] not in positions:
            positions[b[i]] = []
        positions[b[i]].append(i)

    common_prefix_length = 0
    j = 0

    for i in range(n):
        if a[i] not in positions:
            break
        if j >= len(positions[a[i]]):
            break
        if positions[a[i]][j] < i:
            while j < len(positions[a[i]]) and positions[a[i]][j] < i:
                j += 1
            if j >= len(positions[a[i]]):
                break
        if a[i] != b[positions[a[i]][j]]:
            break
        common_prefix_length += 1

    return common_prefix_length


# Read the number of test cases
T = int(input())

for _ in range(T):
    a, b = input().split()
    result = longest_common_prefix(a, b)
    print(result)
