from collections import defaultdict, Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        d = defaultdict(int)
        if n<m:
            return ""
        if t == "":
            return ""
        count = Counter(t)
        left = 0
        min_len = math.inf
        sub_string = [-1,-1]
        have , need = 0, len(count)
        for i in range(n):
            d[s[i]] +=1
            if s[i] in count and count[s[i]] == d[s[i]]:
                have +=1
            while left < n and have == need:               
            
                curr_len = i-left +1
                if min_len> curr_len: 
                    min_len = curr_len
                    sub_string = [left,i]
                d[s[left]] -=1
                if  s[left] in count and count[s[left]] > d[s[left]]:
                    have -=1
                
              
                left +=1
        l,r = sub_string
        return s[l:r+1] if min_len!=math.inf else ""
            
            
        