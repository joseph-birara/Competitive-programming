class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = -1
        
        counts = Counter(nums)
        
        for num in nums:
            if num % 2 ==0:
                if even == -1:
                    even = num
                else:
                    if counts[num] == counts[even]:
                        even = min(even,num)
                    elif counts[num] > counts[even]:
                        even = num
        return even
                
        
        