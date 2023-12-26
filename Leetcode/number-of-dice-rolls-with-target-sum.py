class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        way = [0]
        @cache
        def combination(num, k, tot):
            if num == n:
                return 1 if tot == target else 0

            count = 0
            for i in range(1, k + 1):
                if tot + i <= target:
                    count += combination(num + 1, k, tot + i)

            return count

        way[0] = combination(0, k, 0)
        return way[0] % mod
