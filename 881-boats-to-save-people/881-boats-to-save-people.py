class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people) -1
        i = 0
        res = 0
        while n >= i:
            if people[n] + people[i] <= limit:
                n -=1
                i +=1
                res +=1
            else:
                res +=1
                n -=1
        return res
            
        
        