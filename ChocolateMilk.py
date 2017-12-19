class ChocolateMilk:
    def __init__(self, id):
        self.id = id
        self.price = 2
        self.ingredients = {}
        self.workload = 5

    def __del__(self):
        self.id = None
        self.price = None
        self.ingredients = None

    def getPrice(self):
        return self.price

    def getId(self):
        return self.id

    def addIngredient(self, ingredient, amount):
        if self.ingredients[ingredient] is None:
            self.ingredients[ingredient]=amount
        elif self.ingredients[ingredient] is not None:
            self.ingredients += amount
        self.price += ingredient.price
        self.workload += amount

    def returnWorkload(self):
        return self.workload

