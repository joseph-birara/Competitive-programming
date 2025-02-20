class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        def backtrack(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                else:
                    return
            return backtrack(curr + '1') or backtrack(curr + '0')
        return backtrack("")
            
