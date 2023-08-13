

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(dict)
        length = len(nums)
        max_length = 1

        for i in range(length):
            for j in range(i):
                difference = nums[i] - nums[j]
                if difference not in dp[j]:
                    dp[j][difference] = 1
                if difference not in dp[i]:
                    dp[i][difference] = 0
                dp[i][difference] = dp[j][difference] + 1
                
                max_length = max(max_length, dp[i][difference])
        
        return max_length
