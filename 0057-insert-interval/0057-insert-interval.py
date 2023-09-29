class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        intervals.append(newInterval)
        intervals.sort()
        
        
        
        res = []
        
        preStart , preEnd= intervals[0]
        end = preEnd
        
        for start, end in intervals[1:]:
            if start <=preEnd:
                preEnd = max(end, preEnd)
            else:
                res.append([preStart,preEnd])
                preStart = start
                preEnd = end
        res.append([preStart,max(end,preEnd)])
        return res
        
        