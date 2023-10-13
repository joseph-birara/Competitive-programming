class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = []
        counts = Counter(nums)
        oneThird = len(nums)//3
        
        for key  in counts:            
            if counts[key] >oneThird:
                res.append(key)
        return res
        