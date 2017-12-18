class Marshmallow:
    #Constructor
    #param expiredate: The expirationdate of the marshmallows
    def __init__(self, expiredate):
        self.price = 0.75
        self.expiredate = expiredate

    #Destructor
    def __del__(self):
        self.price = None
        self.expiredate = None

    #Returns the price of this marshmallow
    def getPrice(self):
        return self.price

    #Returns the expirationdate of this marshmallow
    def getExpiredate(self):
        return self.expiredate
