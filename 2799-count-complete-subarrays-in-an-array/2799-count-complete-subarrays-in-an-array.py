class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        length = len(set(nums))
        left = 0
        res = 0
        my_dict = defaultdict(int)

        for index,num in enumerate(nums):
            my_dict[num] += 1
            while len(my_dict) == length and left < len(nums):
                res += len(nums)- index
                if nums[left] in my_dict:
                    my_dict[nums[left]] -= 1
                    if my_dict[nums[left]] == 0:
                        del my_dict[nums[left]]
                left += 1
            
            
                
        return res
