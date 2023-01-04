class Solution:
    def freqAlphabets(self, s: str) -> str:
        
            result = ''
            index= 0
            while index <len(s):
                if index+ 2 < len(s) and s[index+2] =="#":
                    result += chr(int(s[index:index+2]) + ord('a')-1)
                    index +=3
                    
                else:
                    result += chr(int(s[index])+ord('a')-1)
                    index+=1
            return result 
        