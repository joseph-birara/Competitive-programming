class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        degree = 0
        num_frequency = {}
        for i, num in enumerate(nums):
            if num not in num_frequency:
                num_frequency[num] = [i]
            else:
                num_frequency[num].append(i)
            degree = max(degree, len(num_frequency[num]))
        
        min_length = float('inf')
        for num, indices in num_frequency.items():
            if len(indices) == degree:
                min_length = min(min_length, indices[-1] - indices[0] + 1)

        return min_length


        