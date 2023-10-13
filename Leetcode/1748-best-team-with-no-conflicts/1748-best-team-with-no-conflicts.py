class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        players = sorted(zip(scores,ages))       

        dp = [pair[0] for pair in players]
        for i in range(1, len(dp)):
            for j in range(i-1, -1,-1):
                if players[i][1] >= players[j][1]:
                    dp[i]  = max(dp[i], players[i][0] + dp[j])      



        return max(dp)



        