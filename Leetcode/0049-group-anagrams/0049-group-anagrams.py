from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))            
            counts[sorted_word].append(word)
        
        return list(counts.values())
