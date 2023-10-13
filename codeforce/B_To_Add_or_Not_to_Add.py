n, k = map(int, input().split())
arr = sorted(map(int, input().split()))
start = diff = 0
window = 1
max_occurrences = 1
min_element = arr[0]

for j in range(1, n):
    diff += (arr[j] - arr[j - 1]) * window
    window += 1

    while diff > k:
        diff -= arr[j] - arr[start]
        window -= 1
        start += 1

    if window > max_occurrences:
        max_occurrences = window
        min_element = arr[j]

print(max_occurrences, min_element)
