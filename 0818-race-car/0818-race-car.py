class Solution:
    def racecar(self, target: int) -> int:
        
        q = deque()# moves, position, velocity
        q.append((0,0,1))
        
        while q :
            moves ,position, speed = q.popleft()
            if position == target:
                return moves
            q.append((moves+1, position+speed, speed*2))
            
            if (position + speed > target and speed >0)  or (speed <0 and speed + position< target ):
                q.append((moves + 1, position, -speed / abs(speed)))
        return -1 
            
        