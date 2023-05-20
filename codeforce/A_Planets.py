from collections import Counter


testtCase = int(input())

for _ in range(testtCase):
    n, c = map(int, input().split())

    orbits = list(map(int, input().split()))
    cost = 0

    freq = Counter(orbits)

    for key in freq:
        cost += min(freq[key], c)
    print(cost)
