class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        d = {}        
         
        length = len(names)
        
        for index in range (length):
            d[heights[index]] = names[index]
        
        isSwaped = True
        
        for i in range(length-1):
            for j in range(length-(i+1)):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1],heights[j]
                    isSwaped = False
            # if not isSwaped:
            #     break
        temp = []
        for item in heights:
            temp.append(d[item])
        return temp
                
                
        