class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        result =[]
        
        
            
        for word in words:
            word_count_dict = defaultdict(int)
            for c in word:
                word_count_dict[c] +=1
            for w in count:
                
                count[w] = min(count[w], word_count_dict[w])
        for key in count:
            while count[key] >0:
                result.append(key)
                count[key] -=1
                
        return result
            
            
                
                
            
        
        
        