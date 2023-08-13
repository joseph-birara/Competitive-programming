class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
       
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left_pointer, right_pointer = i+1, n-1
            while left_pointer < right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                if current_sum == 0:
                    result.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer+1]:
                        left_pointer += 1
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer-1]:
                        right_pointer -= 1
                    left_pointer += 1
                    right_pointer -= 1
                elif current_sum < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return result

        