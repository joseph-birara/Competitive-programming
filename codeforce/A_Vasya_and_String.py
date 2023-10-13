from collections import defaultdict
n, k = map(int, input().split())
s = input()
left = 0
count = defaultdict(int)
beauty = 0
right = 0
while right < n:
    while right < n and min(count['a'], count['b']) <= k:
        count[s[right]] += 1
        right += 1
    min_temp = min(count['a'], count['b'])
    max_temp = max(count['a'], count['b'])
    beauty = max(beauty, max_temp + min(min_temp, k))
    count[s[left]] -= 1
    left += 1

print(beauty)
