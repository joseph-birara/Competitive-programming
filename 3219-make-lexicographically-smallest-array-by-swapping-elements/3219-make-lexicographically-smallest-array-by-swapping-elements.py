from collections import deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Step 1: Sort the array
        sorted_nums = sorted(nums)

        # Step 2: Initialize grouping
        current_group = 0
        num_to_group_map = {}
        group_to_sorted_values = {}
        group_to_sorted_values[current_group] = deque([sorted_nums[0]])
        num_to_group_map[sorted_nums[0]] = current_group

        # Step 3: Group numbers based on the `limit` condition
        for i in range(1, len(sorted_nums)):
            # If the difference between consecutive numbers is greater than `limit`, start a new group
            if abs(sorted_nums[i] - sorted_nums[i - 1]) > limit:
                current_group += 1

            # Map the current number to its group
            num_to_group_map[sorted_nums[i]] = current_group

            # Add the number to the sorted deque of its group
            if current_group not in group_to_sorted_values:
                group_to_sorted_values[current_group] = deque()
            group_to_sorted_values[current_group].append(sorted_nums[i])

        # Step 4: Replace elements in the original array with the smallest values in their groups
        for i in range(len(nums)):
            current_num = nums[i]
            group = num_to_group_map[current_num]
            nums[i] = group_to_sorted_values[group].popleft()

        return nums
