n,k = map(int,(input().split()))
result =0
theorems = list(map(int,input().split()))
t = list(map(int,input().split()))


min_sum = 0
for indx, num in enumerate(t):
    if num == 1:
        min_sum += theorems[indx]

left = 0
global_max = 0
max_ = 0

for right in range(n):
    if right - left > k-1:
        if t[left] == 0:
            max_ -= theorems[left]
        left += 1
    if t[right] == 0:
        max_ += theorems[right]
    global_max = max(global_max, max_)
print(global_max + min_sum)
    