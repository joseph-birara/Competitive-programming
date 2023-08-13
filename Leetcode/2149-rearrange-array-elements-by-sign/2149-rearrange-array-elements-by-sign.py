class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_elements =[]
        negative_elements =[]
        for element in nums:
            if element >0:
                positive_elements.append(element)
            else:
                negative_elements.append(element)
        mixed_elements =[]
        
        index =0
        while index < len(negative_elements):
            mixed_elements.append(positive_elements[index])
            mixed_elements.append(negative_elements[index])
            index +=1
                
        return mixed_elements