n, c = map(int, input().split())
seconds = list(map(int, input().split()))

result = 1

for i in range(1, n):
    if seconds[i] - seconds[i-1] > c:
        result = 1
    else:
        result += 1
print(result)
