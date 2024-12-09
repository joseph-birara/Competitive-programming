from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Helper function to check parity
        if len(nums) == 1:
            return [True] * len(queries)
        def parity(num):
            return num % 2
        
        n = len(nums)
        
        # Preprocess the same_parity array
        same_parity = [0] * (n - 1)
        for i in range(n - 1):
            if parity(nums[i]) == parity(nums[i + 1]):
                same_parity[i] = 1
        
        # Build prefix sum for same_parity
        prefix_sum = [0] * (n - 1)
        prefix_sum[0] = same_parity[0]
        for i in range(1, n - 1):
            prefix_sum[i] = prefix_sum[i - 1] + same_parity[i]
        
        # Evaluate each query
        result = []
        for fromi, toi in queries:
            # If the range has no adjacent pairs (single element), it's special
            if toi - fromi == 0:
                result.append(True)
                continue
            
            # Calculate the sum of same_parity within the range
            end = toi - 1
            range_sum = prefix_sum[end] - (prefix_sum[fromi - 1] if fromi > 0 else 0)
            
            # If range_sum > 0, subarray is not special
            result.append(range_sum == 0)
        
        return result
