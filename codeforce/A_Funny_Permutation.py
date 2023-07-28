for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print(-1)
    else:
        permutation = list(range(3, n + 1)) + [2, 1]
        print(*permutation)
