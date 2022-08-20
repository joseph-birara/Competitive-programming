class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.big):
            heappush(self.big, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.big, num))
        
        
        
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return float(self.big[0] - self.small[0]) / 2.0
        else:
            return float(self.big[0])
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()