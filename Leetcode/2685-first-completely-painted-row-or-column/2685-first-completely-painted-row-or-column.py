class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        rowFreq = defaultdict(int)
        colFreq = defaultdict(int)
        pos = defaultdict(tuple)
        

        n , m = len(mat), len(mat[0])

        for index in range(n):
            for j in range(m):
                val = mat[index][j]
                pos[val] = (index,j)

        c = len(arr)

        for i in range(c):
            row,col = pos[arr[i]]
            rowFreq[row] += 1
            colFreq[col] += 1

            if rowFreq[row] == m or colFreq[col] == n:
                return i
        return c
        