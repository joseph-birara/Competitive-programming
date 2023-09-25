class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        sum_ = sum(stones)
        target = ceil(sum_ /2)

        def dfs(index, total):
            if total >= target or index == len(stones):
                return abs(total - (sum_-total))
            if (index , total ) in dp:
                return dp[index, total]
            dp[(index,total)] = min(dfs(index+1, total), dfs(index+1, total + stones[index]))
            return dp[(index, total)]


        dp = {}

        return dfs(0,0)


            


        