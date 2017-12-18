class ChocolateMilk:
    #Constructor
    #param id: ID of this chocolatemilk
    def __init__(self, id):
        self.id = id
        self.price = 2
        self.ingredients = None

    #Destructor
    def __del__(self):
        self.id = None
        self.price = None
        self.ingredients = None

    #Returns the price of this chocolatemilk
    def getPrice(self):
        return self.price

    #Returns the price of this chocolatemilk
    def getId(self):
        return self.id

    #Adds ingredients to this chocolatemilk
    def addIngredient(self):
<<<<<<< HEAD
    
    #Returns the amount of workload this chocolatemilk takes
=======

>>>>>>> b445e1b6d83a6626819229d6e55c99571b1191ed
    def returnWorkload(self):
