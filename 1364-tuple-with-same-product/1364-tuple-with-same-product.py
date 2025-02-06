class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                pro = nums[i] * nums[j]
                d[pro] += 1
        ans = 1
        print(d)
        for key, value in d.items():
            if value >1:
                result = math.perm(value, 2)
                ans += result*8
        return (ans-1)//2

        