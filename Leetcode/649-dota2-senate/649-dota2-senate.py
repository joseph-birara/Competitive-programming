class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr = []
        qd = []
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                qr.append(i)
            else:
                qd.append(i)
        while qr and qd :
            indr = qr.pop(0)
            indd = qd.pop(0)
            if indr < indd:
                qr.append(indr + n)
            else:
                qd.append(indd + n)
        return "Radiant" if qr else "Dire"
    
        
        
        
        
        
        
        