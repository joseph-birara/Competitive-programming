class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count_loser = {}
        count_winer= {}
        notLost =[]
        lostOne=[]
        for pair in matches:
            if pair[0] in count_winer.keys():
                count_winer[pair[0]] +=1
            else:
                count_winer[pair[0]] =1
            if pair[1] in count_loser.keys():
                count_loser[pair[1]] +=1
            else:
                count_loser[pair[1]] =1
            
            
        for player in count_winer.keys():
            if player not in count_loser.keys():
                notLost.append(player)
        for player in count_loser.keys():
            if count_loser[player] ==1:
                lostOne.append(player)
        
        return [sorted(notLost),sorted(lostOne)]
                