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
        strin = "Index: " + str(self.ID)+ "\nIngredients: " + str(self.ingredients) + "\nScore: " + str(self.score) + "\nTeam: " + str(self.teamSize)
        return strin    
    
def depthFirst(highScore, pizzas, initialData, index):#recursive
    if pizzas.len = 0 or (initial[1] = 0 and initialData[2] = 0 and initialData[3] = 0):#also needs to account for having enough pizzas for the team size
        return highScore
        
    pizza = pizzas[index]
    pizzas[index] = None
    
    #potentially implement a list of tuples [(pizza type, count),(),()]
    #Go through the teams, deliver the number of pizzas to the team
    #Decrement the count, increment a highScore, go until there are either not enough pizzas or no teams
    #Never deliver same time of pizza to a team
    #Attempt combination of every type of pizza delivered to a team, then next team (decrement team count and pizza type count)
    
    
def depthFirstNaive (highScore, pizzas, initialData):#shift array in every combination of 
    return
    
    
    
def sequentialPizzaAssignment(pizzaCount, pizzas,initialData):
    pIndex = 0
    for i in range(3,0,-1): #go through initialData
        while pizzaCount >= i+1 and initialData[i] > 0:
            #decrement count of pizzas
            
            for j in range(pIndex, pIndex+i+1):#j = index for pizzas running from current pizza and accumulated 
                #print(j)
                pizzas[j].setTeam(i+1)#now all Pizas will know which team they belong to
                pIndex += 1
                pizzaCount -= 1
                    
            initialData[i] -= 1 #decrement count of teams at index
            

ingredientDict = {} #ingredients : score
initialData = [] #[ numPizza, numTwo, numThree, numFour]
pizzas = []

with open("./a_example", "r") as file:
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
    
#sequentialPizzaAssignment(pizzaCount, pizzas,initialData)

#depthFirstSearch
#exhaust all possible combinations to find the optimal result
#select optimal result
#depth first search based on a score generated as pizzas are handed out to teams

highScore = 0

depthFirst(highScore, pizzas, initialData, 0)



        
for p in pizzas:
    print (p)
#print(pizzaCount)
#print (initialData)            
#print (ingredientDict)

    
