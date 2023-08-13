class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        move = 0
        
        while target > 1 and maxDoubles:
            move +=1
            if target%2 :
                target -=1
            else:
                target //=2
                maxDoubles -=1
        


       

        return move + target -1



