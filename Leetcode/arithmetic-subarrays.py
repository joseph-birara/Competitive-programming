class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        temp = []
        m = len(l)
        for i in range(m):
            res = nums[l[i]:r[i]+1]
            var = len(res)
            if var >1:
                res.sort()
                dif = res[1] - res[0]
                bl  = 0
                for k in range(1,var):
                    if (res[k ] - res[k-1]) != dif:
                        bl += 1
                if bl > 0:
                    temp.append(False)
                else:
                    temp.append(True)
                        
                        
        return temp
                        
                        
            
            
                
        
        
        