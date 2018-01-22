class ChiliPepper:
    # Constructor
    # price: Price of chilipepper
    # expiredate: Date the chilipepper will expire
    def __init__(self, expiredate):
        self.price = 0.25
        self.expiredate = int(expiredate)

    # Destructor
    def __del__(self):
        self.price = None
        self.expiredate = None

    # Returns the price of the chilipepper
    def getPrice(self):
        return self.price

    # Returns the expire date of the chilipepper
    def getExpiredate(self):
        return self.expiredate
