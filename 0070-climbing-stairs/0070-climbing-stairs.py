class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Check if result is already computed
        if n in self.memo:
            return self.memo[n]

        # Recursive relation
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
