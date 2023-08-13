class Solution:
    
   
     
    
    def countPairs(self, deliciousness: List[int]) -> int:
        numGoodMeals = 0
        meals = {}
        
        
        for food in deliciousness:
            meals[food] = meals.get(food,0) +1
        for meal in meals:
            for i in range(22):
                diff =( 2**i) - meal
                if diff == meal:
                    numGoodMeals += (meals[meal] * (meals[diff] -1)) //2
                elif diff >= meal and diff in meals :
                    numGoodMeals += meals[diff] * meals[meal]
                
            
            
        return numGoodMeals % ((10**9) +7)
                
        
                
        
        