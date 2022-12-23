class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d= {order[i]:i for i in range(len(order))}
        for i in range(1,len(words)):
            a,b = words[i-1], words[i]
            for j in range(len(a)):
                if j == len(b):
                    return False
                else:
                    al,bl = a[j],b[j]
                    if d[al]<d[bl]:
                        break
                    elif d[al]>d[bl]:
                        return False
        return True