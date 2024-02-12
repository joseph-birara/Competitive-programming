class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        for num in nums:
            d[num]+=1
        
        for key in d:
            
            if d[key] >n//2:
                return key
        
            
        
        
            
        
        
        