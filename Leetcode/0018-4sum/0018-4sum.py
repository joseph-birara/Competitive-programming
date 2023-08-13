class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        nums.sort()
        result = []
        n = len(nums)
        # iterate through the list to get the first element of the quadruplet
        for i in range(n-3):
            # avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # iterate through the list to get the second element of the quadruplet
            for j in range(i+1, n-2):
                # avoid duplicates for the second element
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # initialize left and right pointers
                left_pointer, right_pointer = j+1, n-1
                # use two-pointer technique to find the two remaining elements
                while left_pointer < right_pointer:
                    # calculate the current sum of the four elements
                    current_sum = nums[i] + nums[j] + nums[left_pointer] + nums[right_pointer]
                    if current_sum == target:
                        # add the quadruplet to the result set
                        result.append([nums[i], nums[j], nums[left_pointer], nums[right_pointer]])
                        # move the left pointer to the right while avoiding duplicates
                        while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer+1]:
                            left_pointer += 1
                        # move the right pointer to the left while avoiding duplicates
                        while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer-1]:
                            right_pointer -= 1
                        # move both pointers to continue the search
                        left_pointer += 1
                        right_pointer -= 1
                    elif current_sum < target:
                        # if the current sum is less than the target, move the left pointer to the right
                        left_pointer += 1
                    else:
                        # if the current sum is greater than the target, move the right pointer to the left
                        right_pointer -= 1
       
        return result
