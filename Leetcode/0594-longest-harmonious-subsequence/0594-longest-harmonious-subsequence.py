class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        
        length = 0
        
        for key in count :
            if key + 1 in count :
                length = max(length, count[key] + count[key+1])
        return length 