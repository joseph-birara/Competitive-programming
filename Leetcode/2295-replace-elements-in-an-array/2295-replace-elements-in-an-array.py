class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash_map = {}
        for x, y in reversed(operations):
            
            hash_map[x] = hash_map.get(y, y)
        return [hash_map.get(x, x) for x in nums]
          
        
        