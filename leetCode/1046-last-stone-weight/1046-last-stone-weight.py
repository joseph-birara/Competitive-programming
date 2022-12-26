class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapify(heap)
        while len(heap)>1:
            m = heappop(heap)
            y = heappop(heap)
            if m-y != 0:
                heappush(heap,m-y)
        return -heap[0] if len(heap) == 1 else 0
       