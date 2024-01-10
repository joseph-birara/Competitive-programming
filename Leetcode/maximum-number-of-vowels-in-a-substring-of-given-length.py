class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        count = Counter(s[:k])
        res = self.calculate(count)
        left = 0
        n = len(s)
        for i in range(k,n):
            count[s[left]] -= 1
            count[s[i]] += 1
            left +=1
            res = max(res,self.calculate(count))
        return res

    def calculate(self,d):
        return d['a'] + d['e'] + d['u'] + d['i'] + d['o']
        