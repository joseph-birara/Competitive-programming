class Solution:
    def maxScore(self, s: str) -> int:
        hashmap = Counter(s)
        zero = 0
        one = hashmap['1']
        res = 0
        if s[-1] == '0':
            s = s[:-1]

        for ele in s:
            if ele == '0':
                zero += 1
            else:
                one -= 1
            res = max(res, zero+one)
        return res

        