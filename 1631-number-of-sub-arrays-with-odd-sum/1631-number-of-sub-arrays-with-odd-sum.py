class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
      
        MOD = 10**9 + 7
        n = len(arr)       
        
        odd_count = 0
        even_count = 1
        total_sum = 0       
        
        result = 0
        
        for num in arr:
            total_sum += num
            
            if total_sum % 2 == 0:
                even_count += 1
                result = (result + odd_count) % MOD
            else:
                odd_count +=1
                result = (result + even_count) % MOD
        
        return result

