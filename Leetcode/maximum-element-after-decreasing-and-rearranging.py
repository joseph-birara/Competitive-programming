class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        n = len(arr)

        res = 1
        for i in range(1,n):
            if arr[i] > res +1:
                res +=1
                arr[i] = res
            else:
                res = arr[i]        
         
            


        return max(arr)

        
        