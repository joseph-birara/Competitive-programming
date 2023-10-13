class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        heaters.sort()

        radius = 0


        for i in range(len(houses)):
            left = 0
            right = len(heaters)-1
            temp_radius = float('inf')
            target = houses[i]
           


            while left < right :
                mid = (left + right ) //2

                
                if target == heaters[mid]:
                    temp_radius = 0
                    break
                elif target > heaters[mid]:
                    temp_radius = min(temp_radius, abs(heaters[mid]-target))
                    left = mid + 1
                else:
                    temp_radius = min(temp_radius, abs(heaters[mid]-target))
                    right = mid
            temp_radius = min(temp_radius, abs(heaters[left]-target))
                
            radius = max(radius,temp_radius)
        return  (radius)


        


        
