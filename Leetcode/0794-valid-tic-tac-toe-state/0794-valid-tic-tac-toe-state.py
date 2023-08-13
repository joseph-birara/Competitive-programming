class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        d= defaultdict(int)
        for row in board:
            for c in row:
                d[c] +=1
        if d['X'] - d['O'] >1 or  d['X'] - d['O'] <0 :
            return False
        
        if d['X'] -  d['O'] == 1 :
            if self.checkIfWiner( board,'O'):
                return False
            
        
         
        if d['X'] ==  d['O']:
            if self.checkIfWiner(board,"X"):
                return False
            
        
         
        return True
    
        
        
        
    def checkIfWiner(self, gameBoard ,player):
        gameBoard 
        for i in range(3):
            
            if gameBoard[i][0] == player and  gameBoard[i][1] == gameBoard[i][0] and gameBoard[i][2] == gameBoard[i][1] :
                return True
            
             
            if gameBoard[0][i] == player  and  gameBoard[1][i] == gameBoard[0][i] and  gameBoard[2][i] == gameBoard[1][i] :
                return True
            
             
            if player == gameBoard[0][0] and gameBoard[0][0] == gameBoard[1][1] and  gameBoard[1][1] == gameBoard[2][2]:
                return True
            
             
            if player == gameBoard[0][2] and  gameBoard[1][1] == gameBoard[0][2] and  gameBoard[1][1] == gameBoard[2][0]:
                return True
            
        
         
        return False
    
                