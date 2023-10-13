n = int(input())
hieghts = list(map(int, input().split()))

temp = 0-hieghts[0]
res = min(temp, 0)

for i in range(n-1):
    temp += (hieghts[i] - hieghts[i+1])
    res = min(temp, res)

print(-1*res)
