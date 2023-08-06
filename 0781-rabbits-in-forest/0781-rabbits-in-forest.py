class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        asked = defaultdict(int)
        
        rabits = 0
        
        for answer in answers:
            if not asked[answer]:
                rabits += answer+1
                asked[answer] +=1
            elif asked[answer] == answer +1:
                asked[answer] = 1
                rabits += answer +1
            else:
                asked[answer] += 1
        return rabits
            