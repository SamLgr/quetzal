from CircularLinkedList import CircularLinkedList

class ChocolateMilk:
    # Constructor
    # id: ID to identify chocolate milk in ADTs
    # price: Total price of the chocolate milk
    # ingredients: List with ingredients 'added' to the chocolate milk
    # workload: Total workload of the chocolate milk
    def __init__(self, id):
        self.id = id
        self.price = 2
        self.ingredients = CircularLinkedList()
        self.workload = 5

    # Destructor
    def __del__(self):
        self.id = None
        self.price = None
        self.ingredients = None

    # Returns total price of chocolate milk
    def getPrice(self):
        return self.price

    # Returns ID of chocolate milk
    def getId(self):
        return self.id

    # Adds ingredient object to ingredients in chocolate milk, workload gets incremented and price of ingredient gets added
    def addIngredient(self, ingredient):
        self.ingredients.insert(0, ingredient)
        self.price += ingredient.getPrice()
        self.workload += 1

    # Returns total workload of chocolate milk
    def returnWorkload(self):
        return self.workload
