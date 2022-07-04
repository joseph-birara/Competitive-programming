class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        temp = []
        n = len(nums)
        for i in range(n-1):
            for  j in range(i+1,n):
                if nums[i] == nums[j]:
                    temp.append((i,j))
        return len(temp)
        