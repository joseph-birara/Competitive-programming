class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(int)
        temp =[]
        
        for index , character in enumerate(s):
            d[character] = index
        max_index = d[s[0]]
        left = 0
        for i in range(len(s)):
            max_index =max(d[s[i]],max_index)
            if i == max_index:
                max_index+=1 
                temp.append(max_index -left)
                
                left = max_index
            
        return temp
                
            
        
        