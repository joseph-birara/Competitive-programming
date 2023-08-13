class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas)- sum(cost)<0:
            return -1
        index = 0
        summ = 0
        
        for i in range(len(cost)):
            summ += (gas[i] - cost[i])
            if summ <0:
                index = i+1
                summ = 0
        return index
    
   