class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = ''

        for i in s:
            if i.isalnum():
                d+=i.lower()
        i=0
        k=len(d)-1
        print(d)
        while k>=i:
            if d[i]!=d[k]:
                return False
            i =i+1
            k =k-1
        return True