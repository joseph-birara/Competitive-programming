from collections import Counter
_, goal = [*map(int, input().split())]
a=[*map(int, input().split())]
 
counts = Counter(a).items()
 
val = []
for m,l in counts:
for i in range(1,l+1):
val.append((m, l//i))
 
s = sorted(val, key=lambda x: x[1])[-goal:]
 
res = [m for m,l in s]
print(*res)