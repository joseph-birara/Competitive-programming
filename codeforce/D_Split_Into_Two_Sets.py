def can_divide_dominoes(n, dominoes):
    num_occurrences = {}

    for a, b in dominoes:
        num_occurrences[a] = num_occurrences.get(a, 0) + 1
        num_occurrences[b] = num_occurrences.get(b, 0) + 1

    for occurrences in num_occurrences.values():
        if occurrences > 2:
            return "NO"

    return "YES"


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    dominoes = [tuple(map(int, input().split())) for _ in range(n)]

    result = can_divide_dominoes(n, dominoes)
    print(result)
