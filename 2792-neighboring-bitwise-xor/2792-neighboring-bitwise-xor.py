class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        def is_valid(start_value):
            
            original = [0] * n
            original[0] = start_value            
            
            for i in range(1, n):
                original[i] = original[i - 1] ^ derived[i - 1]            
            
            return original[-1] ^ original[0] == derived[-1]

        
        return is_valid(0) or is_valid(1)
            



        
        