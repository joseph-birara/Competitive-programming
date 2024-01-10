class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        left = 0
        n = len(answerKey)
        d = defaultdict(int)   
        confuse = 0     

        for right in range(n):
            d[answerKey[right]] += 1            
            while min(d['T'],d['F']) >k and left < right:
                d[answerKey[left]] -= 1
                left += 1
            factor = max(d['T'],d['F']) + k if max(d['T'],d['F']) + k <=n else n
            confuse = max(factor , confuse)
        return confuse
            
            

                
        