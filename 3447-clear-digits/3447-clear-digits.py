class Solution:
    def clearDigits(self, s: str) -> str:
        pair = defaultdict(int)
        indexes = []
        n = len(s)
        

        for i in range(n):
            if '0' <= s[i] <= '9':
                if indexes :
                    ind = indexes.pop()
                    pair[ind] = i
            else:
                indexes.append(i)
        ans = ''
        for i in range(n):
            if '0' <= s[i] <= '9' or i in pair:
                continue
            ans+= s[i]
        return ans


        
        
            




        
        