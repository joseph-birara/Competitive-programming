class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def count_nigh(row,col,n,m):
            one = 0
            zero = 0
            drxn = [(-1,-1),(-1,0,),(-1,1),(0,1),(0,-1),(1,0),(1,-1),(1,1)]
            for x,y in drxn:
                nex = x+row
                ney = col +y
                if 0<=nex<n and 0<=ney <m:
                    if temp[nex][ney] == 1:
                        one +=1
                    else:
                        zero +=1
            return [zero,one]
            
            
            
        
        temp = copy.deepcopy(board)
        n, m = len(board), len(board[0])
        
        for i in range(n):
            for j in range(m):
                zero, one = count_nigh(i,j,n,m)
                
                if board[i][j] == 1:
                    if one <2  or one >3:
                        board[i][j] = 0
                else:
                    if one == 3:
                        board[i][j] = 1
                    
                        
                    
        