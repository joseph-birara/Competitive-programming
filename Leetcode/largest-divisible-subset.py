class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()

        # Initialize dynamic programming arrays
        dp = [1] * len(nums)
        prev_index = [-1] * len(nums)

        # Iterate over the array
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev_index[i] = j

        # Find the index of the maximum element in dp array
        max_index = dp.index(max(dp))
        
        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev_index[max_index]

        return result[::-1]
        