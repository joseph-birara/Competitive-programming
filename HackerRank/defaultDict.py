# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,(input().split()))
d = defaultdict(list)
a = []
for inp in range(n):
    a.append(input())
b = []
for inp in range(m):
    b.append(input())
for index,val in enumerate(a):
    if val in b:
             
        d[val].append(index+1)
for i in b:
    if i in a:
        print(' '.join(map(str, d[i])))
    else:
        print(-1)
