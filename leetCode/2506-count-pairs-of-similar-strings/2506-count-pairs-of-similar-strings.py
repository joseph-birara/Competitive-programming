class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordSet=[]
        for word in words :
            s=set()
            for c in word:
                s.add(c)
            wordSet.append(s)
        res =0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if  wordSet[i] ==  wordSet[j]:
                    res+=1
        return res
                    
        
            
        