class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 :
            return []

        visited = set((0,0))
        pairs = []
        heap = []
        n = len(nums1)
        m = len(nums2)

        heappush(heap,(nums1[0]+ nums2[0],0,0))        
        
        while len(pairs)<k  and heap:            
            dummy , i, j = heappop(heap)
            pairs.append([nums1[i],nums2[j]])
            if i + 1 < n and (i+1, j) not in visited:
                heappush(heap,(nums1[i+1]+ nums2[j],i+1,j))
                visited.add((i+1,j))
            if j + 1 < m and (i,1+j) not in visited:
                heappush(heap,(nums1[i]+ nums2[j+1],i,1+j))
                visited.add((i,1+j))
        
        return pairs
        



        