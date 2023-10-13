n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
nums = zip(h1, h2)
a, b = 0, 0
for x, y in nums:
    a, b = max(a, b+x), max(b, a+y)

print(max(a, b))
