class Piza:
    def __init__(self, ingredients, ID, ingCount):
        self.ingredients = ingredients#list of ingredients text
        self.ID = ID
        self.ingCount = ingCount
        teamSize = -1
        self.score = 0
    
    def ingredientScoreCalc(self):
        for item in self.ingredients:
            self.score += 1/ingredientDict[item]
            
    def setTeam(self, teamSize):
        self.teamSize = teamSize
            
            
    def __str__(self):
        strin = "\nIngredients: " + str(self.ingredients) + "\nScore: " + str(self.score) + "\nTeam: " + str(self.teamSize)
        return strin
    
    
def output():
    return
            

ingredientDict = {} #ingredients : score
initialData = [] # numPizza, numTwo, numThree, numFour
pizzas = []


with open("a_example", "r") as file:
    fileData = file.readlines()
    initialData = [int(x) for x in fileData[0].split()]
    for index,lineData in enumerate(fileData[1:]):#(index,lineData) 
        ingCount = lineData.split()[0:1]
        ingredients = lineData.split()[1:]
        pizza = Piza(ingredients, index, ingCount[0])
        pizzas.append(pizza)
        
        for ing in ingredients:
            if ing in ingredientDict:
                ingredientDict[ing] += 1
                
            else:
                ingredientDict[ing] = 1
        index += 1 
        
pizzaCount = initialData[0]        
for piza in pizzas:
    piza.ingredientScoreCalc()
    
pIndex = 0
for i in range(3,0,-1): 
    while pizzaCount >= i+1 and int(initialData[i]) > 0:
        initialData[i] -= 1 #decrement count of teams at index
        pizzaCount -= 1 #decrement count of pizzas
        
        for j in range(pIndex, pIndex+i+1):#j = index for pizzas running from current pizza and accumulated 
            try:
                pizzas[j].setTeam(i+1)#now all Pizas will know which team they belong to
                pIndex += 1
            
            except IndexError:#no more pizzas
                break
    
        
        
for p in pizzas:
    print (p)
print (initialData)            
print (ingredientDict)

    
