class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
       
        n = len(arr)
        total_sum = 0
        
        for start in range(n):
            for length in range(1, n - start + 1, 2):
                end = start + length
                total_sum += sum(arr[start:end])
        
        return total_sum

        