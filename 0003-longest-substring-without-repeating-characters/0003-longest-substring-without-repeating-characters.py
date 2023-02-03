class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_len = 0
        max_len = 0
        str_result=''
        
        for c in s:
            if c not in str_result:
                 str_result +=c
            else:
                 str_result =  str_result[ str_result.index(c)+1:]+c
            current_len = len( str_result)
            
                
            max_len= max(current_len, max_len)
        return max_len
            
        