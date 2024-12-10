class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        
        # Function to check if a substring is special
        def is_special(sub):
            return len(set(sub)) == 1
        
        # Start with the longest possible substring length
        for length in range(n, 0, -1):
            count = {}
            
            # Generate all substrings of the current length
            for i in range(n - length + 1):
                sub = s[i:i + length]
                
                # Check if the substring is special
                if is_special(sub):
                    count[sub] = count.get(sub, 0) + 1
            
            # Check if any substring occurs at least three times
            for sub, freq in count.items():
                if freq >= 3:
                    return length
        
        # If no special substring is found, return -1
        return -1
