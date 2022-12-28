class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        length = len(nums)
        temp=[0]*length
        temp[0]=nums[0]
        res=deque([(temp[0],0)])
        for i in range(1,length):
            temp[i]=res[0][0]+nums[i]
            while res and temp[i]>res[-1][0]:
                res.pop()
            res.append((temp[i],i))
            if res[0][1]<=i-k:
                res.popleft()
        return temp[-1]
            
        
        