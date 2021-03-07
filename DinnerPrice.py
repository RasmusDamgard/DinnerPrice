class Ingredient:
    def __init__(self, name, unitprice, unitname):
        self.Name = name
        self.UnitPrice = unitprice
        self.UnitName = unitname

    def __eq__(self,ingredient2):
        return self.Name == ingredient2.Name

    def __str__(self):
        return self.Name
#a recipe is a list of tuples each containing (Ingredient, Amount)

class Dish:
    def __init__(self, name, recipe):
        self.Name = name
        self.Recipe = recipe
        self.IngredientList = [tup[0] for tup in recipe]

    def __str__(self):
        return self.Name

    def Price(self):
        price = 0

        for point in self.Recipe:
            ingredient = point[0]
            amount = point[1]
            price += ingredient.UnitPrice * amount
        return price

    def HasIngredient(self, ingredientUse):
        return ingredientUse in self.IngredientList


    def PrintIngredients(self):
        for i in range(len(self.Recipe)):
            print("  Item #{0}: {1} {2} of {3}".format(i, self.Recipe[i][1], self.Recipe[i][0].UnitName, self.Recipe[i][0].Name))

ingredients = {
    "rice": Ingredient("rice", 3.25, "kg"),
    "pasta": Ingredient("pasta", 4, "kg"),
    "bacon": Ingredient("bacon", 4, "kg"),
    "cream": Ingredient("cream", 3, "l"),
    "cheese": Ingredient("cheese", 3, "kg"),
    "oil": Ingredient("oil", 0.25, "l")
}

dishes = {
    "carbonara": Dish("Spaghetti Carbonara", [
        (ingredients["pasta"], 1),
        (ingredients["cream"], 0.5),
        (ingredients["cheese"], 2),
        (ingredients["bacon"], 2)
    ])
    #"fried rice":
}

spaghettiCarbonara = dishes["carbonara"]

dishesVar = {
    "spaghettiCarbonara": spaghettiCarbonara
}

def TransformToVar(string):
    string = string.lower()
    string = string.strip(" ")
    raiseChar = string.rfind(" ")
    if raiseChar != -1:
        char  = string[raiseChar+1]
        char  = char.upper()
        string = string[:raiseChar+1] + char + string[raiseChar+1 + 1:]
    string = string.replace(" ", "")
    return string

isDone = False 
while not isDone:
    action = input("What do you want to do?")
    action = action.lower()
    action = action.strip()
    if action == "tell":
        dish = input("What dish do you want the ingredients of?")
        dish = TransformToVar(dish)
        if dish not in list(dishesVar.keys()):
            print("That is not a dish")
            continue
        print(dishesVar[dish].PrintIngredients())
        ##Den er har en ekstra
        break
    elif action == "price":
        dish = input("What dish do you want the price of?")
        dish = TransformToVar(dish)
        if dish not in list(dishesVar.keys()):
            print("That is not a dish")
            continue
        print(dishesVar[dish].Price())
        break
    elif action == "use":
        ingredientString = input("What ingredient do you want to use?")
        while not ingredientString in ingredients:
            ingredientString = input("What ingredient do you want to use?")

        ingredient = ingredients[ingredientString]
        useAmount = input("How much {0} do you want to use? In {1}".format(ingredient.Name, ingredient.UnitName))
        useAmount = useAmount.replace(",", ".")
        useAmount = float(useAmount)
        ####hvad gør man her?

        containsIngredient = {}
        for dish in dishes.values(): 
            print(dish)
            print(dish.IngredientList)
            for i in range(len(dish.Recipe)):
                if dish.Recipe[i][0] == ingredient:
                    formerAmount = dish.Recipe[i][1]
                    if formerAmount < useAmount:
                        useAmount = formerAmount
                    newPrice = dish.Price()-useAmount*ingredient.UnitPrice
                    print(dish.Price())
                    print(newPrice)
                    containsIngredient[dish] = newPrice
        print(containsIngredient)
        break
    else:
        print("Not a valid input")
        continue

#make dish name pretty
#make sure u can only input the intended type
#smart måde at lave nye dishes og ingredients med google sheets