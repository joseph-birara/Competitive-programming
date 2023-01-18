class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000   }
        result =0
        n = len(s)
        count = 0
        
        while count < n:
            if count < n-1:
                if s[count] == "I" and s[count+1] == "V":
                    result +=4
                    count +=2
                elif s[count] == "X" and s[count+1] == "L":
                    result += 40
                    count +=2
                elif s[count] == "X" and s[count+1] == "C":
                    result += 90
                    count +=2
                elif s[count] == "I" and s[count+1] == "X":
                    result += 9
                    count +=2
                elif s[count] == "C" and s[count+1] == "D":
                    result += 400
                    count +=2
                elif s[count] == "C" and s[count+1] == "M":
                    result += 900
                    count +=2
                else:
                    result += d[s[count]]
                    count +=1
            else:
                result +=d[s[count]]
                count +=1
        return result 
        
        
        