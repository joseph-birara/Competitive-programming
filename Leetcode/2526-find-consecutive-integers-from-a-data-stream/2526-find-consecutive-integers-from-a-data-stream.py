class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.data =0
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.data +=1
            
        else:
            self.data =0
        return self.data >= self.k
            
        
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)