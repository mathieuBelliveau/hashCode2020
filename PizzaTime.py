class Piza:
    def __init__(self, ingredients, ID):
        self.score = 0
        self.ingredients = ingredients
        self.ID = ID
        teamSize = -1
    
    def ingredientScoreCalc(self):
        for item in self.ingredients:
            self.score += 1/ingredientDict[item]
            
    def setTeam(teamSize):
        self.teamSize = teamSize
            
            
    def __str__(self):
        strin = "\nIngredients: " + str(self.ingredients) + "\nScore: " + str(self.score)
        return strin
    
    
def output():
    return
            

ingredientDict = {} #ingredients : score
initialData = [] # numPizza, numTwo, numThree, numFour
pizzas = []
pizzasDelivered = 0


with open("a_example", "r") as file:
    fileData = file.readlines()
    #initialData = fileData[0].split()
    initialData = [int(x) for x in fileData[0].split()]
    #index = 0 #0 index for Piza id
    for index,data in enumerate(fileData[1:]):
        ingredients = data.split()[1:]
        pizza = Piza(ingredients, index)
        pizzas.append(pizza)
        
        for ing in ingredients:
            if ing in ingredientDict:
                ingredientDict[ing] += 1
                
            else:
                ingredientDict[ing] = 1
        index += 1        
for piza in pizzas:
    piza.ingredientScoreCalc()
    
count = int(initialData[0])
pIndex = 0
for i in range(3,0,-1): 
    while count >= i+1 and int(initialData[i]) > 0:
        pizzasDelivered += 1
        initialData[i] -= 1
        
        for j in range(pIndex, pIndex+i+1):
            pizzas[pIndex].setTeam(i+1)
        
        pIndex += 1
    
        
        
for p in pizzas:
    print (p)
print (initialData)            
print (ingredientDict)

    
