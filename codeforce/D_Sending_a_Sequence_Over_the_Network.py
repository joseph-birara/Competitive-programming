for _ in range(int(input())):
    n = int(input())
    sequence = list(map(int, input().split()))
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(n):
        if i - sequence[i] >= 0 and dp[i - sequence[i]]:
            dp[i + 1] = True
        if i + sequence[i] + 1 <= n and dp[i]:
            dp[i + sequence[i] + 1] = True

    print(['NO', 'YES'][dp[-1]])
