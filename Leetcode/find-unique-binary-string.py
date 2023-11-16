class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = [int(ele, 2) for ele in nums]
        res = 0
        print(nums)

        for i in range(18):
            if i not in nums:
                res = i
                break
        print(res)
        n = len(nums)
        temp = bin(res)
        m = len(temp) - 2

        return '0' * (n-m ) + temp[2:]

        