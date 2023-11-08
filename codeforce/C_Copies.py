from math import ceil

n, x, y = map(int, input().split())

small = min(x, y)
big = max(x, y)


def possible(t, n, x, y):

    if t < small:
        return False
    t -= small
    n -= 1
    temp = t//x + t//y
    return temp >= n


high = small * n
low = 0

while low + 1 < high:
    mid = (low+high)//2
    if possible(mid, n, x, y):
        high = mid
    else:
        low = mid

print(high)
