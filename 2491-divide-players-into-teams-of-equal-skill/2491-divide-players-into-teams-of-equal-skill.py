class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        print(skill)
        last = len(skill)-1
        first = 0
        sum_ = skill[0]+skill[last]
        chemistry = 0
        while first < last:
            if sum_ !=skill[first]+skill[last]:
                return -1
            else:
                chemistry +=skill[first]*skill[last]
                last -=1
                first +=1
        return chemistry
                
            