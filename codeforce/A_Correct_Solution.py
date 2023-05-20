from heapq import heapify, heappop

n = list(input())
m = list(input())


heapify(n)
temp = []
res = []
while n and n[0] == "0":
    num = heappop(n)
    temp.append(num)

if n:
    res.append(heappop(n))
for i in temp:
    res.append(i)
while n:
    res.append(heappop(n))

if res == m:
    print("OK")

else:
    print("WRONG_ANSWER")
