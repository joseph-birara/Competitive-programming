class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        ds={}
        dt={}
        for i in s:
            if i not in ds.keys():
                ds[i]=1
            else:
                ds[i]+=1
        for i in t:
            if i not in dt.keys():
                dt[i]=1
            else:
                dt[i]+=1
        for k in t:
            if k not in ds.keys() or ds[k]<dt[k]:
                return k
                