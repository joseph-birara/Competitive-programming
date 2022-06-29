class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        nums.sort()
        arr = []
        for i in range(l):
            if nums[i] == target:
                arr.append(i)
        return arr
                