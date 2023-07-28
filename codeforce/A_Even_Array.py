
test = int(input())
for i in range(test):
    mode1 = 0
    mode0 = 0
    n = int(input())

    array = list(map(int, input().split()))

    for index, num in enumerate(array):
        if index % 2 != num % 2:
            if index % 2 == 0:
                mode0 += 1
            else:
                mode1 += 1
    if mode0 == mode1:
        print(mode1)
    else:
        print(-1)
