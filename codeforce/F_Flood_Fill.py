n = int(input())
seq = [int(i) for i in input().split()]

unique_seq = []
for num in seq:
    if not unique_seq or unique_seq[-1] != num:
        unique_seq.append(num)

n = len(unique_seq)
rev_seq = unique_seq[::-1]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        if rev_seq[i] == unique_seq[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

min_removals = n - 1 - dp[n][n] // 2

print(min_removals)
