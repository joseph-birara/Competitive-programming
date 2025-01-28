class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0
        for  word in words:
            if s.startswith(word):
                cnt += 1
        
        
        return cnt
        