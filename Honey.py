class Honey:
    #Constructor
    #param expiredate: Expiration date of the honey
    def __init__(self, expiredate):
        self.price = 0.5
        self.expiredate = int(expiredate)

    #Destructor
    def __del__(self):
        self.price = None
        self.expiredate = None

    #Returns the price of this honey
    def getPrice(self):
        return self.price

    #Returns the expiration date of this honey
    def getExpiredate(self):
        return self.expiredate
