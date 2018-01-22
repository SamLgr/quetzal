class ChocolateShot:
    # Constructor
    # shottype: Type of the chocolate shot
    # price: Price of the chocolate shot
    # expiredate: The expire date of the chocolate shot
    def __init__(self, shottype, expiredate):
        self.shottype = shottype
        self.price = 1
        self.expiredate = int(expiredate)
    
    # Destructor
    def __del__(self):
        self.shottype = None
        self.price = None
        self.expiredate = None

    # Returns the type of the chocolate shot
    def getType(self):
        return self.shottype
    
    # Returns the price of the chocolate shot
    def getPrice(self):
        return self.price

    # Returns the expire date of the chocolate shot
    def getExpiredate(self):
        return self.expiredate
