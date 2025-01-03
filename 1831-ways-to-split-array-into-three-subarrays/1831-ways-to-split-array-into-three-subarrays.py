class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Step 1: Compute prefix sum
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        if prefix[-1] == 0:  # Total sum is 0
            return ((n - 1) * (n - 2) // 2) % MOD
        result = 0
        
        # Step 2: Iterate over the left split point
        for i in range(n-2):
            if prefix[i] > prefix[-1] - prefix[i]:
                break  # If left is already greater than total, no further splits are possible
            
            # Step 3: Use two pointers for the mid-subarray
            # Find the smallest valid `j_left`
            j_left = bisect_left(prefix, 2 * prefix[i], i+1)
            # Find the largest valid `j_right`
            j_right = bisect_right(prefix, (prefix[i] + prefix[-1]) // 2, j_left) - 1
            
            if j_left <= j_right and j_right < n - 1:
                result += j_right - j_left + 1
        
        return result % MOD
