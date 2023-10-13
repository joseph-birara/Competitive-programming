# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        # find the peach index
        low = 1
        high = mountain_arr.length()-2
        max_high = high
        res = -1
        peack = 0
        while low<= high:
            mid = (low+high) //2
            print(1,mid)
            mid_ele = mountain_arr.get(mid)
            right = mountain_arr.get(mid+1)
            left = mountain_arr.get(mid-1)
            if left <= mid_ele >= right:                
                peack = mid
                break
            elif right >= mid_ele:
                low = mid +1
            else:
                high = mid -1
        #for the right part
        low = peack 
        high = mountain_arr.length()-1
        

        while low<= high:
            mid = (low+high) //2
            print(2,mid)
            mid_ele = mountain_arr.get(mid)                 
            
            if mid_ele == target:                
                res = mid
                high = mid-1
            elif target> mid_ele:
                high = mid - 1
            else:
                low = mid +1

        #for the left part
        low = 0
        high = peack
        while low<= high:
            mid = (low+high) //2
            print(3,mid)
            mid_ele = mountain_arr.get(mid)              
            
            if mid_ele == target:                
                res = mid
                high = mid-1
            elif target> mid_ele:
                low = mid + 1
            else:
                high = mid -1
        return res
        
        
        
                
            


        
        
