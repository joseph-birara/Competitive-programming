import math


n,m,a = input().split()
x = math.ceil(int(n)/int(a))
y = math.ceil(int(m)/int(a))
print(x*y)