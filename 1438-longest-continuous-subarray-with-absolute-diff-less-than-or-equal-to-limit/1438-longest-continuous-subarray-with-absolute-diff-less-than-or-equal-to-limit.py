class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        ma , mi, = nums[0], nums[0]
        res = 1
        start = 0
        end = 0
        temp = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            mi = min(mi,nums[i])
            ma = max(ma,nums[i])
            if abs(ma-mi) <=limit:
                temp.append(nums[i])
                
            else:
                
                del temp[0]
                temp.append(nums[i])
                mi = min(temp)
                ma = max(temp)
            res = max(len(temp),res)
        return res
            
                
                
            
            
        