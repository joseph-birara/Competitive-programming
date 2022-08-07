class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count= Counter(words)
        heap = [(-x[1], x[0]) for x in count.items()]
        
        heapify(heap)
        
        temp = []
        
        while len(temp) < k:
            temp.append(heappop(heap)[1])
        
        return temp
        