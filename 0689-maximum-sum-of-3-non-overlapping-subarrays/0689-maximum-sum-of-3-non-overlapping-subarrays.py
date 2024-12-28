class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
            
        n = len(nums)
        
        # Step 1: Compute sums of all subarrays of length k
        window_sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        window_sums[0] = current_sum
        for i in range(1, len(window_sums)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sums[i] = current_sum

        # Step 2: Compute max sums for left and right
        left = [0] * len(window_sums)
        right = [0] * len(window_sums)
        
        # Fill left array
        max_index = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[max_index]:
                max_index = i
            left[i] = max_index

        # Fill right array
        max_index = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[max_index]:  # >= ensures lexicographic order
                max_index = i
            right[i] = max_index

        # Step 3: Iterate through all valid middle intervals and track the max sum
        max_sum = 0
        result = []
        for mid in range(k, len(window_sums) - k):
            l = left[mid - k]
            r = right[mid + k]
            current_sum = window_sums[l] + window_sums[mid] + window_sums[r]
            if current_sum > max_sum:
                max_sum = current_sum
                result = [l, mid, r]

        return result


        