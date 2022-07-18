class Solution:
    def decodeString(self, s: str) -> str:
        temp = []
        ch = []
        
        n = len(s)
        for i in range(n):
            count = 0
            
            if s[i].isdigit():
                k = i
                while (s[k] >= '0' and s[k] <= '9'):
                    count = count * 10 + ord(s[k]) - ord('0')
                    k += 1
                
                    
                     
                if  i > 0 :
                    if (s[i-1].isdigit()  == False):
                        temp.append((count))
                elif i == 0:
                    temp.append((count))
                    
                                
            
            elif s[i] == ']' and temp:
                ind = int(temp.pop())
                res = ''
                while ch[-1] != '[':
                    res = ch[-1] + res
                    ch.pop()
                ch.pop()
                ch.append(res*ind)
            else:
                ch.append(s[i])
        return ''.join(ch)
                
                
                
                
        
        