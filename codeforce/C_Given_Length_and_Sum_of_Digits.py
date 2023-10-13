length, total = map(int, input().split())
min_num = []
min_total = total
max_total = total
max_num = []
if total > 9*length or (total < 1 and length != 1):
    print(-1, -1)
else:
    flag = False
    for i in range(0, length):
        if min_total > 9:
            min_num.append('9')
            min_total -= 9
        elif i < length - 1 and min_total >= 1:
            min_num.append(str(min_total-1))
            min_total = 0
            flag = True
        else:
            min_num.append(str(min_total))
            min_total = 0
    if flag and min_num:
        min_num[-1] = '1'
    elif flag:
        min_num.append('-1')

    # max number
    for i in range(0, length):
        if max_total >= 9:
            max_num.append('9')
            max_total -= 9
        else:
            max_num.append(str(max_total))
            max_total = 0
    final_min = -1
    final_max = -1
    if min_num:
        final_min = int(''.join(min_num[::-1]))
    if max_num:
        final_max = int(''.join(max_num))

    print(final_min, final_max)
