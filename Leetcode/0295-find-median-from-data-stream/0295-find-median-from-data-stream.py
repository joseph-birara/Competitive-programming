class MedianFinder:

    def __init__(self):
        self.right = []   
        self.left = []
        

    def addNum(self, num: int) -> None:
               
        if len(self.left) == len(self.right):
                       
            heappush(self.left,-heappushpop(self.right,num))                    
             
        else:
            heappush(self.right,-heappushpop(self.left,-num))              
                     

    def findMedian(self) -> float:
        
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2.0
        else:
            return -self.left[0]
                
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()