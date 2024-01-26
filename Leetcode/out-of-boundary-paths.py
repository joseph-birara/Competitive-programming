class Solution:
    def findPaths(self, m: int, n: int, N: int, startRow: int, startCol: int) -> int:
        MOD = 1000000000 + 7
        current_paths = [[0] * n for _ in range(m)]
        current_paths[startRow][startCol] = 1
        total_paths = 0

        for moves in range(1, N + 1):
            new_paths = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        total_paths = (total_paths + current_paths[i][j]) % MOD
                    if j == n - 1:
                        total_paths = (total_paths + current_paths[i][j]) % MOD
                    if i == 0:
                        total_paths = (total_paths + current_paths[i][j]) % MOD
                    if j == 0:
                        total_paths = (total_paths + current_paths[i][j]) % MOD
                    new_paths[i][j] = (
                        ((current_paths[i - 1][j] if i > 0 else 0) + (current_paths[i + 1][j] if i < m - 1 else 0)) % MOD +
                        ((current_paths[i][j - 1] if j > 0 else 0) + (current_paths[i][j + 1] if j < n - 1 else 0)) % MOD
                    ) % MOD

            current_paths = new_paths

        return total_paths
