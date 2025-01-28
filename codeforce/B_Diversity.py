

#Calculate the minimum number of characters you need to change in the string s, so that it contains at least k different letters, or print that it is impossible.

#String s consists only of lowercase Latin letters, and it is allowed to change characters only to lowercase Latin letters too.
#Input: A string s and an integer k.
#Output: The minimum number of characters you need to change in the string s, so that it
# contains at least k different letters, or print that it is impossible.



from typing import Counter


def min_change(s,k):
    
    d = Counter(s)

    if len(s) < k:
        return "impossible"

    
    
    if len(d) >= k:

        return 0
    else:
        return k - len(d)

s = input()
k = int(input())
print(min_change(s,k)) 

