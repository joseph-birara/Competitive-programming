n, d = map(int, input().split())

power = list(map(int, input().split()))
power.sort(reverse=True)

left = 0
right = n-1
win_count = 0
pow_sum = 0
temp = n
while temp > 0:
    pow_sum += power[left]
    temp -= 1
    if pow_sum > d:
        win_count += 1
        left += 1
        pow_sum = 0
print(win_count)
