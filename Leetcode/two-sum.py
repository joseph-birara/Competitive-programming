class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hasmap = defaultdict(int)
        for index , num in enumerate(nums):
            temp = target - num
            if temp in hasmap:
                return [hasmap[temp],index]
            hasmap[num] = index
        