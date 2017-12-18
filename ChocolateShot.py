class ChocolateShot:
    #Constructor
    #param type: Type of choclateshot
    #param expiredate: The expirationdate of the shot
    def __init__(self, type, expiredate):
        self.type = type
        self.price = 1
        self.expiredate = expiredate
    
    #Destructor
    def __del__(self):
        self.type = None
        self.price = None
        self.expiredate = None

    #Returns the type of this shot
    def getType(self):
        return self.type
    
    #Returns the price of this shot
    def getPrice(self):
        return self.price

    #Returns the expirationdate of this shot
    def getExpiredate(self):
        return self.expiredate
