class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        n = len(s1)
        diff1 =''
        diff2 =''

        for i  in range(n):
            if s1[i] != s2[i]:
                diff1 += s1[i]
                diff2 += s2[i]

        k =  len(diff1)
        if k == 1 or k > 2:
            return False
        if k == 2 and sorted(diff1) == sorted(diff2):
            return True
        if k == 2 :
            return False
        return True
        