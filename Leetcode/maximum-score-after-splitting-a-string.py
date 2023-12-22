class Solution:
    def maxScore(self, s: str) -> int:

        hashmap = Counter(s)
        zero = 0
        one = hashmap['1']
        if s[-1] == '0':
            s = s[:-1]
        # if one == 0:
        #     return len(s) -1

        res = 0

        for sub in s:
            if sub == '0':
                zero += 1
            else:
                one -= 1            
            res = max(one + zero,res)
        

        return res






        