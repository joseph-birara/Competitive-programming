import heapq
from math import sqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:        
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):            
            num = -heapq.heappop(gifts)            
            back = int(sqrt(num))            
            heapq.heappush(gifts, -back)
        
        return -sum(gifts)
