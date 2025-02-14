class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
        elif not self.nums:
            self.nums = [num]
        else:
            self.nums.append(num * self.nums[-1])

    def getProduct(self, k: int) -> int:
        if len(self.nums) < k:
            return 0
        if k == len(self.nums):
            return self.nums[-1]
        return self.nums[-1] // self.nums[-k - 1]  
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)