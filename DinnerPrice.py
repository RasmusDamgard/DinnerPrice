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

Carbonara = dishes["carbonara"]

print(Carbonara.Price())



def IsStringValid(dish):
    dishLower = dish.lower()
    if dishLower in list(dishes.keys()):
        return True
    return False

usefullInput = False 
while not usefullInput:
    userDish = input("What dish do you want to make?")
    if IsStringValid(userDish):
        break
