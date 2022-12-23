class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index=-1
        distance= math.inf
        for ind,point in enumerate(points):
            if point[0]==x or point[1]==y:
                mahtan=abs(x-point[0]) + abs(y-point[1])
                if mahtan<distance:
                    index= ind
                    distance =mahtan
        return index
                
        