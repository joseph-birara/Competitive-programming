class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        start_end = defaultdict(list)
        res = 0

        for i in range(len(s)):
            l = s[i]
            if start_end[l] and len(start_end[l]) == 2:
                start_end[l][-1] = i
            else:
                start_end[l].append(i)

        for key in start_end:
            if len(start_end[key]) == 2:
                start, end = start_end[key]
            else:
                continue
            d = defaultdict(int)
            for i in range(start+ 1, end):
                d[s[i]] = 1
            res += len(d)
        return res