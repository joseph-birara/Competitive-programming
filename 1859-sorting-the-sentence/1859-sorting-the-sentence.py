class Solution:
    def sortSentence(self, s: str) -> str:
        arr=s.split()
        n=len(arr)
        temp=[None]*n
        for i in range(n):
            item=arr[i]
            temp[int(item[-1])-1]=item[:-1]
        
        return ' '.join(temp)
        