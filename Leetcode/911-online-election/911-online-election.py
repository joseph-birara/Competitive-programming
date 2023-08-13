class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leadVoted = [0] * len(times)
        count = Counter()
        currentlead = persons[0]
        
        for i, (person, time) in enumerate(zip(persons, times)):
            count[person] += 1
            if count[person] >= count[currentlead]:
                currentlead = person
            self.leadVoted[i] = (time, currentlead)

    def q(self, t: int) -> int:
        start, end = 0, len(self.leadVoted) - 1
        
        while start <= end:
            mid = (start + end) // 2
            time, lead = self.leadVoted[mid]
            if time == t:
                return lead
            if time < t:
                start = mid + 1
            else:
                end = mid - 1

        time, lead = self.leadVoted[end]
        return lead
                
        
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)