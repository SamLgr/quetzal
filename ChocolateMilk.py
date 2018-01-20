from CircularLinkedList import CircularLinkedList

class ChocolateMilk:
    def __init__(self, id):
        self.id = id
        self.price = 2
        self.ingredients = CircularLinkedList()
        self.workload = 5

    def __del__(self):
        self.id = None
        self.price = None
        self.ingredients = None

    def getPrice(self):
        return self.price

    def getId(self):
        return self.id

    def addIngredient(self, ingredient):
        self.ingredients.insert(0, ingredient)
        self.price += ingredient.getPrice()
        self.workload += 1

    def returnWorkload(self):
        return self.workload
