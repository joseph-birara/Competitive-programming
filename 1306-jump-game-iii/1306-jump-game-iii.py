class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        Q = collections.deque()
        Q.append(start)
        temp = set()
        while Q:
            ind = Q.popleft()
            if arr[ind] == 0:
                return True
            for m in ((ind+arr[ind]),(ind-arr[ind])):
                if 0 <= m < len(arr) and m not in temp:
                    Q.append(m)
                    temp.add(ind)
        return False 
                
        