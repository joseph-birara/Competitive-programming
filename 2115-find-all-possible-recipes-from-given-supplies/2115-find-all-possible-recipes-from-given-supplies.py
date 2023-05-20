

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe_ingredient_pairs = list(zip(recipes, ingredients))
        ingredient_recipe_graph = defaultdict(list)
        recipe_indegrees = {r: 0 for r in recipes}
        
        # Build the ingredient-recipe graph and calculate recipe indegrees
        for recipe, ing in recipe_ingredient_pairs:
            for ingredient in ing:
                ingredient_recipe_graph[ingredient].append(recipe)  # parent is the ingredient required to make the child recipe 
                if ingredient not in supplies:
                    recipe_indegrees[recipe] += 1  # if ingredient is not present, the child recipe is dependent
        
        # Perform topological sorting using a queue
        queue = deque()
        possible_recipes = []
        
        # Initialize the queue with recipes having zero indegree
        for recipe, indegree in recipe_indegrees.items():
            if indegree == 0:
                queue.append(recipe)
                possible_recipes.append(recipe)
        
        # Process the recipes in the queue and update indegrees
        while queue:
            current_recipe = queue.popleft()
            for neighbor_recipe in ingredient_recipe_graph[current_recipe]:
                recipe_indegrees[neighbor_recipe] -= 1
                if recipe_indegrees[neighbor_recipe] == 0:
                    possible_recipes.append(neighbor_recipe)  # the parent recipe was possible to make, so now the child recipe can be made too
                    queue.append(neighbor_recipe)
        
        return possible_recipes

        
        