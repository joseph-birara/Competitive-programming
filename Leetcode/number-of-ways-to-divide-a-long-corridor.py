class Solution:
    def numberOfWays(self, corridor: str) -> int:

        num = Counter(corridor)['S']
        if num <2 or num % 2 == 1:
            return 0
        n = len(corridor)
        res = 1
        num_s = 0
        start = 0
        for i in range(n):
            if corridor[i] == 'S' and num_s == 2:
                num_s  = 1
                res *= (i-start)
            elif corridor[i] == 'S':
                num_s += 1
                if num_s == 2:
                    start = i
            


        return res % (10**9 + 7)