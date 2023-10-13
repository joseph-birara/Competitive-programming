class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors)<3:
            return False
        n = len(colors)
        alic = 0
        bob = 0
        count_a = 0
        count_b = 0
        for i in range(n):
            if  colors[i]  == 'A':
                count_a +=1
                if count_b >2:
                    bob += (count_b-2)
                count_b = 0
            elif   colors[i]  == 'B':
                count_b += 1
                if count_a >2 :
                    alic += (count_a -2)
                count_a = 0
        if count_b >2:
            bob += (count_b-2)
        if count_a >2 :
            alic += (count_a -2)

        
        return alic >bob
