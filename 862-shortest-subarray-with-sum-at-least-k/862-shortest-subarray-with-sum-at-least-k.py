class Solution:
    import collections
    def shortestSubarray(self, nums: List[int], k: int) -> int:
       
        n = len(nums)
        pre_sums = [0]
        for i in range(n):
            pre_sums.append(nums[i]+pre_sums[-1])
        mono_q = collections.deque()
        ans = n+1
        for idx,s in enumerate(pre_sums):
            while mono_q and s-pre_sums[mono_q[0]] >=k:
                ans = min(ans,idx -mono_q.popleft() )
            while mono_q and s <= pre_sums[mono_q[-1]]:
                mono_q.pop()
            mono_q.append(idx)
        return ans if ans < n+1 else -1
            
       
                
             
            
        