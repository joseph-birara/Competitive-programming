testCAse = int(input())

for i in range(testCAse):
    s = int(input())

    num = ""

    start = 9
    sum_digit = 0

    while start > 0 and sum_digit < s:
        if sum_digit + start < s:
            num = str(start) + num
            sum_digit += start
        elif sum_digit + start == s:
            num = str(start) + num
            break
        start -= 1
    print(num)
