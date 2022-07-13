from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sort_nums = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        temp = []
        for i in range(k):
            temp.append(sort_nums[i][0])
            
        
        return temp
        
        