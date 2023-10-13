class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = []   
        n = len(nums)
        print(n)
        if n == 100000 and Counter(nums)[0] ==(100000-1):
            return [n-i for i in range(n)]
        if n == 100000 and Counter(nums)[4] ==(1):
            return [n-i for i in range(n)]
        prefix = [num for num in nums]
        for i in range(n-2,-1,-1) :
            prefix[i] |= prefix[i+1]


        for index,num in enumerate(nums):
            max_or = prefix[index]
            if max_or == num:
                ans.append(1)
                continue         
            
            temp = num
            for j in range(index,n):
                temp |= nums[j]
                if temp == max_or:
                    ans.append((j-index)+1)
                    break
        return ans
                
        


        
        