class ChiliPepper:
    #Constructor
    #expiredate: Date the chilipepers will expire
    def __init__(self, expiredate):
        self.price = 0.25
        self.expiredate = int(expiredate)

    #Destructor
    def __del__(self):
        self.price = None
        self.expiredate = None

    #Returns the price of the chilipepper
    def getPrice(self):
        return self.price

    #Returns the expirationDate
    def getExpiredate(self):
        return self.expiredate
