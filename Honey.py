class Honey:
    # Constructor
    # price: Price of the honey
    # expiredate: Expire date of the honey
    def __init__(self, expiredate):
        self.price = 0.5
        self.expiredate = int(expiredate)

    # Destructor
    def __del__(self):
        self.price = None
        self.expiredate = None

    # Returns the price of the honey
    def getPrice(self):
        return self.price

    # Returns the expire date of the honey
    def getExpiredate(self):
        return self.expiredate
