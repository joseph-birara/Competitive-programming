class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a= min(len(word1),len(word2))
        res=''
        for i in range(a):
            res+=word1[i]
            res+=word2[i]
        if len(word1)>len(word2):
            res+=word1[a:]
        elif len(word1)<len(word2):
            res+=word2[a:]
        return res
            
        
        