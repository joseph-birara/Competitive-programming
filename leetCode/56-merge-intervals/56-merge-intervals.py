class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        temp = []
        intervals.sort(key = lambda point: point[0])
        n = len(intervals)
        temp.append(intervals[0])
        for i in range(1, n):
            
            if temp[-1][1] >= intervals[i][0] and temp[-1][1] <intervals[i][1] :
                temp[-1][1] = intervals[i][1]
                
            else:
                if temp[-1][1] < intervals[i][1]:
                    temp.append(intervals[i])
        return temp
        