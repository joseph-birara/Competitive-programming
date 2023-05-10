testcase = int(input())
for _ in range(testcase):

    n, x = map(int, input().split())

    start = 0

    faverite = list(map(int, input().split()))

    for num in faverite:
        if num <= x:
            start += num
    fav_set = set(faverite)
    sum_ = x*(x+1)//2

    print(sum_ - 2*start)
