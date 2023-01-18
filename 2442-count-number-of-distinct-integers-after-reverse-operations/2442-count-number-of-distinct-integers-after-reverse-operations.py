class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for index in range(n):
            num = nums[index]
            reversed_num =0
            while num !=0:
                reminder = num%10
                reversed_num = reversed_num * 10 + reminder
                num = num//10
            nums.append(reversed_num)
        return len(set(nums))
        