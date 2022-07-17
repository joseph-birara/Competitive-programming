class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        temp = [i for i in range(1,n+1)]
        i =0
        while len(temp) > 1 :
            n = len(temp)
            i = (i+k-1) % n
            temp.pop(i)
                   
            
            
            
        return temp[0]
            
        