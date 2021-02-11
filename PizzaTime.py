from collections import Counter

class Piza:
    def __init__(self, ingredients, ID, ingCount):
        self.ingredients = ingredients#list of ingredients text
        self.ID = ID
        self.ingCount = ingCount
        teamSize = -1
        self.score = 0
        
    def getIngredientsTuple():
        return tuple(ingredients)
    
    def ingredientScoreCalc(self):
        for item in self.ingredients:
            self.score += 1/ingredientDict[item]
            
    def setTeam(self, teamSize):
        self.teamSize = teamSize
            
            
    def __str__(self):
        strin = "Index: " + str(self.ID)+ "\nIngredients: " + str(self.ingredients) + "\nScore: " + str(self.score) + "\nTeam: " + str(self.teamSize)
        return strin    

#neededForTeam = how many pizzas still need to be delivered for the current team 0 and up
#firstPizza = index of pizza you start looking from in pizzaList    
def depthFirst(neededForTeam, firstPizza):#recursive
    #grab PizzaList assuming format [(type,count),...]
    #also use initialData
    if neededForTeam == 0:
        for i in range(2, 5):#go through teams, delivering i pizzas
            if initialData[i-1] > 0:
                initialData[i-1] -= 1 #decrement team to reserve position
                depthFirst(i, 0)#this is set to 0 to allow all pizzas to be picked up when the combinations start at index 1 and above
                initialData[i-1] += 1 #to come back recursively
    else:
        nextPizza = findFirstNonEmpty(firstPizza)
        while nextPizza >= 0:#at this node, you can pick many different pizzas, so we're essentially finding every combination of them
            temp = pizzaList[nextPizza]
            pizzaList[nextPizza] = (temp[0], temp[1]-1)#replace the count (tuples are immutable)
            depthFirst(neededForTeam-1,firstPizza+1)#found one pizza for this set of combinations for this node, let's find another one
            pizzaList[nextPizza] = temp
            nextPizza = findFirstNonEmpty(nextPizza+1)#to find the next pizza in line for our while loop
    
def findFirstNonEmpty(pizzaIndex):
    while pizzaIndex < len(pizzaList):
        if pizzaList[pizzaIndex][1] > 0:
            return pizzaIndex
        else:
            pizzaIndex += 1
    
    return -1
        
    #function (pizzaStructure, index, number of pizzas to be delivered to team)
    #potentially implement a list of tuples [(pizza type, count),(),()]
    #Go through the teams, deliver the number of pizzas to the team
    #Decrement the count, increment a highScore, go until there are either not enough pizzas or no teams
    #Never deliver same time of pizza to a team
    #Attempt combination of every type of pizza delivered to a team, then next team (decrement team count and pizza type count)
    #Implementation: recursive function takes in # pizzas still selected for a team, and the first pizza that it's allowed to select 
    
    #New Implementation (more efficient)
    #We can assume that the first team will always take the first pizza
    #NOTE we are evaluating combinations and not permutations, as teams don't have an identity and therefore we can't order them
    #
    

ingredientDict = {} #ingredients : score
initialData = [] #[ numPizza, numTwo, numThree, numFour]
#pizzas = []
pizzaList = Counter()

with open("./a_example", "r") as file:
    fileData = file.readlines()
    initialData = [int(x) for x in fileData[0].split()]#first line
    
    
    
    for index,lineData in enumerate(fileData[1:]):#(index,lineData) 
        ingCount = lineData.split()[0:1]
        ingredients = lineData.split()[1:]
        ingredients.sort() 

        pizzaList [tuple(ingredients)] += 1

pizzaCount = initialData[0]       
pizzaList = list(pizzaList.items())
depthFirst(0,0)

    
