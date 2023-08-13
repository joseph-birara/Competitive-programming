class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        res = []
        for i in num:
            while res and k and res[-1]>i:
                res.pop()
                k -=1
            res.append(i)
        res = res[:len(res) - k]
        result = ''.join(res)
        if result :
            return str(int(result))
        return "0"
            
        
        
        
            
        