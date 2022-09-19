

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        drxn = [[1,0],[0,1],[-1,0],[0,-1]]
        N, i, j, pq, res = len(grid) - 1, 0, 0, [], grid[0][0]
        while i < N or j < N:
            for a,b in drxn:
                ia, jb = i + a, j + b
                if ia < 0 or ia > N or jb < 0 or jb > N or grid[ia][jb] > 2500: continue
                heappush(pq, (grid[ia][jb] << 12) + (ia << 6) + jb)
                grid[ia][jb] = 3000
            nxt = heappop(pq)
            res = max(res, nxt >> 12)
            i = (nxt >> 6) & ((1 << 6) - 1)
            j = nxt & ((1 << 6) - 1)
        return res