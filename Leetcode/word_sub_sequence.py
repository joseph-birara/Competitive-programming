class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        n = len(s)
        def sub_sequence(word):
            i = 0
            j = 0
            m = len(word)

            while i<m and j<n:
                if s[j] == word[i]:
                    i +=1
                j += 1
            return m == i
        
        valid = set()
        invalid = set()
        res = 0
        for word in words:
            if word in valid:
                res +=1
            elif word in invalid:
                continue
            elif sub_sequence(word):
                res +=1
                valid.add(word)
            else:
                invalid.add(word)
        return res
            


        
