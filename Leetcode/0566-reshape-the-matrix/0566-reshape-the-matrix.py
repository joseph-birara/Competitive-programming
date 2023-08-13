class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        if len(mat)*len(mat[0]) != r*c:
            return mat
        newMat = []
        temp = []
        
        for row in mat:
            for element in row:
                temp.append(element)
        for newRow in range(r):
            newMat.append(temp[newRow*c:newRow*c +c])
                
        return newMat
                
        
        
        