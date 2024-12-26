class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dp(tot,index):
            if index == n:
                if tot == target :
                    return 1
                return 0
            if (tot,index) in memo:
                return  memo[(tot,index)]
            num = nums[index]
            memo[(tot,index)] = dp(tot+num, index+1) + dp(tot-num, index+1)

            return memo[(tot,index)]

        return dp(0,0)
            
        