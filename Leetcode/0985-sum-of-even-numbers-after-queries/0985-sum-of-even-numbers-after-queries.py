class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = []
        temp_sum =0
        
        for element in nums:
            if element %2 ==0:
                temp_sum += element
        for query in queries:
            if nums[query[1]] %2 ==0:
                if query[0] %2 ==0:
                    temp_sum += query[0]
                else:
                    temp_sum -=nums[query[1]]
            else:
                if query[0] %2 !=0:
                    temp_sum += query[0] + nums[query[1]]
            nums[query[1]] = nums[query[1]] + query[0]
            even_sum.append(temp_sum)
        return even_sum
                    
                
                
        
        