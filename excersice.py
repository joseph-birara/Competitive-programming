class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        self.arr = arr
        self.capacity = capacity
        self.length = length
    # write your code here
    def insertEnd(self, value):
        if self.length <self.capacity:
            self.arr[self.capacity] =value
            self.length +=1
            
    # write your code here
    def removeEnd(self):
        if self.length >0:
            self.arr[self.length-1] = 0
            self.length -=1
        
    # write your code here
    def insertMiddle(self, index, value):
        if self.length <self.capacity:
            self.arr = self.arr[:index] + [value] + self.arr[index:]
            self.length +=1

    # write your code here, you need to shift elements after insertion
    def removeMiddle(self, index):
         self.arr = self.arr[:index]  + self.arr[index+1:]
         self.length -=1

    # write your code here, you need to shift elements after removal

    def printArr(self):
        print(''.join(self.arr))
    # write your code here


