class Solution:
    def numTeams(self, ratings: List[int]) -> int:

        n = len(ratings)
        res = 0     

        for i in range(n):     
            
            rgt = 0
            rls = 0   
            lgt = lls = 0
            for k in range(i):                
                if ratings[i] > ratings[k]:
                    lgt +=1                
                if ratings[i] < ratings[k]:
                    lls +=1        
            for k in range(i+1,n):                
                if ratings[i] > ratings[k]:
                    rgt +=1                
                if ratings[i] < ratings[k]:
                    rls +=1
            res += (lls*rgt + lgt*rls)
            
        return res
                

        

        

        


        
