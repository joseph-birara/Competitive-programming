testcases = int(input())
for _ in range(testcases):
    l, r = map(int, input().split())
    flag = False
    if l == 1:
        print(1, r)
        continue

    for i in range(l, r):
        for num in range(i*2, r+1):
            if num % i == 0:
                print(i, num)
                flag = True
                break
        if flag:
            break
