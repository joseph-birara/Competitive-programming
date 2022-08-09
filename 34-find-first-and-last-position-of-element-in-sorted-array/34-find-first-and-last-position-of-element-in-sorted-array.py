class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        n = len(nums) 
        end = n 
        temp = []
        while start < end:
            mid = (end + start) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1 
            if nums[mid] == target:
                start = end = mid
                while start > 0 and nums[start-1] == target:
                    start -=1
                while end < n-1 and nums[end+1] == target:
                    end +=1
                temp.append(start)
                temp.append(end)
                return temp
        return [-1,-1]
                
                
            
            
        
        