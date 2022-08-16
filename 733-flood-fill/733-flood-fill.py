class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def fill(sr,sc):
            nonlocal x
            
            if sr < 0 or sc < 0 or sr >= len(image) or sc >=len(image[0]) or image[sr][sc] !=x or (sr,sc) in visited:
                return
            image[sr][sc] = color
            visited.add((sr,sc))
            fill(sr+1,sc)
            fill(sr-1,sc)
            fill(sr,sc+1)
            fill(sr,sc-1)
        visited = set()
        
        x = image[sr][sc]
        fill(sr,sc)
        return image
        
        
            
        