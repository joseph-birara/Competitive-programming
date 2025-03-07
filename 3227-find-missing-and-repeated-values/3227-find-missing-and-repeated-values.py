class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        pair = [-1,-1]
        seen = set()

        for row in grid:
            for num in row:
                if num in seen:
                    pair[0] = num
                seen.add(num)
            
        n = len(grid)
        for num in range(n*n +1):
            if num not in seen:
                pair[-1] = num
        return pair
        