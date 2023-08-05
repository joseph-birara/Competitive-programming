class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
            
        # Create a frequency table
        freq_table = {}
        for num in nums:
            freq_table[num] = freq_table.get(num, 0) + 1
      
        prev_points = 0
        curr_points = 0
        
        for num in sorted(freq_table):
            if num - 1 not in freq_table:
                prev_points, curr_points = curr_points, curr_points + num * freq_table[num]
            else:
                prev_points, curr_points = curr_points, max(prev_points + num * freq_table[num], curr_points)

        return curr_points

        
        
        
        