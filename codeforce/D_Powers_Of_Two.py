n, k = map(int, input().split())
values = [1] * k
remaining_value = n - k
index = 0
 
while index < k and remaining_value:
    while values[index] <= remaining_value:
        remaining_value -= values[index]
        values[index] *= 2
    index += 1
 
if remaining_value:
    print('NO')
else:
    print('YES')
    print(*values)