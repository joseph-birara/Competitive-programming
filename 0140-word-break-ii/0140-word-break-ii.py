class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        memo = {}
        res = []

        def dfs(index):
            if index == len(s):
                return [[]]
            if index in memo:
                return memo[index]            
            parts = []
            for i in range(index+1, len(s)+1):
                word = s[index:i]
                if word in wordDict:
                    words =  dfs(i)
                    for txt in words:                       
                        parts.append([word] + txt)
             
            memo[index]  = parts       
            return parts
        res = dfs(0)              

        return [' '.join(word) for word in res]





        