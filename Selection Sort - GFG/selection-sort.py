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
            
            
        
        #code here
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends