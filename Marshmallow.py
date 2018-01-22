class Marshmallow:
    # Constructor
    # price: Price of the marshmallow
    # expiredate: Expire date of the marshmallows
    def __init__(self, expiredate):
        self.price = 0.75
        self.expiredate = int(expiredate)

    # Destructor
    def __del__(self):
        self.price = None
        self.expiredate = None

    # Returns the price of the marshmallow
    def getPrice(self):
        return self.price

    # Returns the expire date of the marshmallow
    def getExpiredate(self):
        return self.expiredate
