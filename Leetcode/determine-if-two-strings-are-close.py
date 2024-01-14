class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n = len(word1)
        m = len(word2)

        if m != n:
            return False  

        

        if set(word1) !=set( word2) :
            return False
        word1 = Counter(word1)
        word2 = Counter(word2)

        return sorted(word1.values()) == sorted(word2.values())
        
        
        
        

        
        