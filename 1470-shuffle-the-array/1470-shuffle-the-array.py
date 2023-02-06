class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        temp =[]
        for index in range(n):
            temp.append(nums[index])
            temp.append(nums[index+n])
        return temp
        