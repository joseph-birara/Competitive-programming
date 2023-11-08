input()
previous_num, count = 3, 0
for current_num in list(map(int, input().split())):
    if current_num == previous_num and previous_num != 3:
        current_num = 0
    elif current_num == 3 and previous_num != 3:
        current_num -= previous_num
    if current_num == 0:
        count += 1
    previous_num = current_num
print(count)
