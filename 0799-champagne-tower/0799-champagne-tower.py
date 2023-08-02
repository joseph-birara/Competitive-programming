class Solution:
    
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0.0] * (r + 1) for r in range(query_row + 1)]
        glasses[0][0] = poured

        for i in range(query_row):
            for j in range(len(glasses[i])):
                if glasses[i][j] > 1:
                    excess_champagne = glasses[i][j] - 1
                    glasses[i][j] = 1
                    glasses[i + 1][j] += excess_champagne / 2
                    glasses[i + 1][j + 1] += excess_champagne / 2

        return min(1, glasses[query_row][query_glass])
