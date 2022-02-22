class Solution: # 83, 45
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Topological sort
        remainders = {} # Unresolved-recipe -> set{blocker-ingredients}
        supplyBlockerToRecipe = collections.defaultdict(set) # Blocker-ing -> Impacted-recipies
        newIngredients = [] # In each new round, newly unlocked ingredient
        ans = []
        supplies = set(supplies)
        
        # Record unreachable recipes and their blockers, record in 2 dicts
        for rec, ings in zip(recipes, ingredients):
            remainingIngs = set(ings) - supplies # Find out what is missing
            if not remainingIngs: # Nothing is missing, recipe good to go
                ans.append(rec)
                newIngredients.append(rec) # Recipe unlocked as ingredient
            else: # Part of ingredients missing, record blocker
                remainders[rec] = remainingIngs
                for ing in remainingIngs:
                    supplyBlockerToRecipe[ing].add(rec)
                    
        while newIngredients: # Each round we unlock new recipes as newIngredients
            newNewIngredients = [] # newly unlocked ones in this round
            for ing in newIngredients: # for each new ingredient
                for rec in supplyBlockerToRecipe[ing]: # what WAS this new ingredient previously blocking
                    remainders[rec].remove(ing) # remove the registered blocker
                    if not remainders[rec]: # no more blockers, this recipe is good to go
                        ans.append(rec)
                        newNewIngredients.append(rec) # register recipe as new ingredient
                supplyBlockerToRecipe[ing].clear()
            newIngredients = list(newNewIngredients)
        
        return ans
            