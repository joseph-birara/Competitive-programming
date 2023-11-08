class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        res = [0]*(100+1)

        for birth, death in logs:
            birth -= 1950
            death -= 1950

            res[birth] +=1
            res[death] -=1
        for i in range(1,100):
            res[i] += res[i-1]
        num = max(res)

        return res.index(num) + 1950


        