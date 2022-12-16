class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n= len(matrix)
        k= len(matrix[0])
        res=[]
        for j in range(k):
            temp =[]
            for i in range(n):
                temp.append(matrix[i][j])
            res.append(temp)
       

        return res