class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-x for x in nums]
        heapify(h)
        while k>1:
            heappop(h)
            k -=1
        return -1 * h[0]
                
        
        
        