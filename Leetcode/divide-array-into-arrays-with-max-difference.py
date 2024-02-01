class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(0,n-2,3):
            if abs(nums[i] - nums[i+2] ) >k:
                return []
            else:
                temp = [nums[i],nums[i+1], nums[i+2]]
                ans.append(temp)
        return ans

        
        