

n, p = map(int, input().split())
arr = list(map(int, input().split()))

curr_start = 0
min_len = 1
curr_sum = arr[0]
left = 0

for i in range(1, n):
    curr_sum += arr[i]
    while left < i and curr_sum - arr[left] >= p:
        curr_sum -= arr[left]
        min_len = min(i-left, min_len)
        left += 1
        curr_start = left

print(curr_start, min_len)
