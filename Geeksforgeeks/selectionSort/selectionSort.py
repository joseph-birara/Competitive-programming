#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        min = i
        for k in range(i+1, len(arr)):
            if arr[k] < arr[min]:
                min = k
                
            
        return min
    
    def selectionSort(self, arr,n):
        for i in range(n):
            ind = self.select(arr,i)
            if ind != i:
                arr[ind], arr[i] = arr[i], arr[ind]
        return arr
            
            