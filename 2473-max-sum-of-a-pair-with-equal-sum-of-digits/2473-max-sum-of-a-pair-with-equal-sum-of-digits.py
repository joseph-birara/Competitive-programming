class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        d = defaultdict(list)
        n = len(nums)

        for i in range(n):
            num = str(nums[i])
            tot = 0
            for char in num:
                tot += int(char)
            d[tot].append(nums[i])
        ans = -1

        for key, value in d.items():
            l = len(value)
            if l >= 2:
                value.sort()
                ans = max(value[-2] + value[-1], ans)
        return ans


    


        