class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        key = keysPressed[0]        
        duration = releaseTimes[0]
        
        for i in range(1, len(keysPressed)):
            temp = releaseTimes[i] - releaseTimes[i-1]
            
            if temp >duration:
                key = keysPressed[i]
                duration = temp
            elif temp == duration:
                key = max(key, keysPressed[i])
        return key
            
        