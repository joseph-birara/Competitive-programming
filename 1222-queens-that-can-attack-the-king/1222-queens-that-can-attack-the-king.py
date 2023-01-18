class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        temp = []
        
        for up_down in [-1,0,1]:
            for left_right in [-1,0,1]:
                for distance in range(1,8):
                    row = king[0] + distance*up_down
                    col = king[1] + distance * left_right
                    if [row,col] in queens :
                        temp.append([row,col])
                        break
        return temp
                        
                
                
        
        