class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def delta(p, t):
            return (p + 1) / (t + 1) - p / t

        
        heap = [(-delta(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        
        for _ in range(extraStudents):
            
            d, p, t = heapq.heappop(heap)
            
            p, t = p + 1, t + 1
            
            heapq.heappush(heap, (-delta(p, t), p, t))

        
        total_ratio = sum(p / t for _, p, t in heap)  
        return total_ratio / len(classes)
