class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=Counter(tasks)
        freq=sorted(list(counter.values()))

        max_idle=freq.pop()
        total=(max_idle-1)*n

        while freq and total>0:
            total=total-min(max_idle-1,freq.pop())

        total=max(0,total)
        return len(tasks) + total
        
        
        