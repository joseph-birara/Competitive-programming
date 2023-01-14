class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        moves = []
        num_move = 0
        
        n = len(boxes)
        for index in range(n):
            num_move =0
            for index2 in range(n):
                if boxes[index2] == "1":
                    num_move += abs(index -index2)
            moves.append(num_move)
        return moves
                    
        
        