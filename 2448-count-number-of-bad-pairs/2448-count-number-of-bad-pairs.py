class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        d = defaultdict(int)
        for ind, num in enumerate(nums):
            nums[ind] = ind - num
        count = 0
        

        for ind, num in enumerate(nums):
            
            count += ((ind) - d[num])
            d[num] += 1

        return count


        