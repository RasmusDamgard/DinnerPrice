class Ingredient:
    def __init__(self, name, unitprice, unitname):
        self.Name = name
        self.UnitPrice = unitprice
        self.UnitName = unitname

#a recipe is a list of tuples each containing (Ingredient, Amount)

class Dish:
    def __init__(self, name, recipe):
        self.Name = name
        self.Recipe = recipe

    def Price(self):
        price = 0
        for point in self.Recipe:
            ingredient = point[0]
            amount = point[1]
            price += ingredient.UnitPrice * amount
        return price

    def IngredientList(self):
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
        print(dishesVar[dish].IngredientList())
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
        print("use")
        break
    else:
        print("Not a valid input")
        continue