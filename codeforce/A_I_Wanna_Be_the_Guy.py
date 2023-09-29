n = int(input())

p = list(map(int, input().split()))
y = list(map(int, input().split()))

length = p[0] + y[0]

passed = p[1:] + y[1:]

if set(passed) == set(list(range(1, n+1))):
    print("I become the guy.")
else:

    print("Oh, my keyboard!")
