class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowHash = defaultdict(int)
        colHash = defaultdict(int)

        n,m = len(grid), len(grid[0])
        isolated = 0
        total = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    total += 1
                    rowHash[i] += 1
                    colHash[j] += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if  rowHash[i] == 1 and  colHash[j] ==1:
                        isolated += 1
        return total - isolated

                
        

        