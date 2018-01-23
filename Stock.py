from StockTable import StockTable
from ChocolateShot import ChocolateShot
from Honey import Honey
from Marshmallow import Marshmallow
from ChiliPepper import ChiliPepper

class Stock:
    # Constructor
    # chocolatestock: Stock table with chocolate shots
    # honeystock: Stock table with honey
    # marshmallowstock: Stock table with marshmallows
    # chilipepperstock: Stock table with chilipeppers
    def __init__(self, chocolatestock=StockTable(), honeystock=StockTable(), marshmallowstock=StockTable(), chilipepperstock=StockTable()):
        self.chocolatestock = chocolatestock
        self.honeystock = honeystock
        self.marshmallowstock = marshmallowstock
        self.chilipepperstock = chilipepperstock

    # Destructor
    def __del__(self):
        self.chocolatestock = None
        self.honeystock = None
        self.marshmallowstock = None
        self.chilipepperstock = None

    # Returns chocolate shot stock table
    def getChocolatestock(self):
        return self.chocolatestock

    # Returns honey stock table
    def getHoneystock(self):
        return self.honeystock

    # Returns marshmallow stock table
    def getMarshmallowstock(self):
        return self.marshmallowstock

    # Returns chilipepper stock table
    def getChilipepperstock(self):
        return self.chilipepperstock

    # Sets chocolate shot stock table to given chocolate shot stock table
    def setChocolatestock(self, chocolatestock):
        self.chocolatestock = chocolatestock

    # Sets honey stock table to given honey stock table
    def setHoneystock(self, honeystock):
        self.honeystock = honeystock

    # Sets marshmallow stock table to given marshmallow stock table
    def setMarshmallowstock(self, marshmallowstock):
        self.marshmallowstock = marshmallowstock

    # Sets chilipepper stock table to given chilipepper stock table
    def setChilipepperstock(self, chilipepperstock):
        self.chilipepperstock = chilipepperstock

    # Deletes oldest ingredient from stock with given stock type
    def stockDelete(self, stockType):
        if stockType == "white chocolate":
                self.chocolatestock.tableDeleteOldestShot("white")
        elif stockType == "milk chocolate":
                self.chocolatestock.tableDeleteOldestShot("milk")
        elif stockType == "brown chocolate":
                self.chocolatestock.tableDeleteOldestShot("brown")
        elif stockType == "black chocolate":
                self.chocolatestock.tableDeleteOldestShot("black")
        elif stockType == "honey":
                self.honeystock.tableDeleteOldest()
        elif stockType == "marshmallow":
                self.marshmallowstock.tableDeleteOldest()
        elif stockType == "chilipepper":
                self.chilipepperstock.tableDeleteOldest()

    # Returns a list with all items in the stock table for every ingredient
    def stockTraverse(self):
        traverselist = []
        traverselist.extend(self.chocolatestock.traverseTable())
        traverselist.extend(self.honeystock.traverseTable())
        traverselist.extend(self.marshmallowstock.traverseTable())
        traverselist.extend(self.chilipepperstock.traverseTable())
        return traverselist

    # Add given amount of ingredients to stock with given stock type
    def stockOrder(self, stockType, amount):
        if stockType == "white chocolate":
            while amount != 0:
                chocolate = ChocolateShot("white", 5)
                self.chocolatestock.tableInsert(chocolate)
                amount-=1
        elif stockType == "milk chocolate":
            while amount != 0:
                chocolate = ChocolateShot("milk", 5)
                self.chocolatestock.tableInsert(chocolate)
                amount-=1
        elif stockType == "brown chocolate":
            while amount != 0:
                chocolate = ChocolateShot("brown", 5)
                self.chocolatestock.tableInsert(chocolate)
                amount-=1
        elif stockType == "black chocolate":
            while amount != 0:
                chocolate = ChocolateShot("black", 5)
                self.chocolatestock.tableInsert(chocolate)
                amount-=1
        elif stockType == "honey":
            while amount != 0:
                honey = Honey(5)
                self.honeystock.tableInsert(honey)
                amount-=1
        elif stockType == "marshmallow":
            while amount != 0:
                marshmallow = Marshmallow(5)
                self.marshmallowstock.tableInsert(marshmallow)
                amount-=1
        elif stockType == "chilipepper":
            while amount != 0:
                chilipepper = ChiliPepper(5)
                self.chilipepperstock.tableInsert(chilipepper)
                amount-=1 

    # Checks if amount in a specific stock is too low and orders accordingly
    def stockCheck(self):
        #ChocolateStock
        traverselist = self.chocolatestock.traverseTable()
        milkcounter = 0
        whitecounter = 0
        blackcounter = 0
        browncounter = 0
        for choco in traverselist:
            if choco.getType() == "milk chocolate":
                milkcounter += 1
            if choco.getType() == "white chocolate":
                whitecounter += 1
            if choco.getType() == "black chocolate":
                blackcounter += 1
            if choco.getType() == "brown chocolate":
                browncounter += 1

        if milkcounter < 2:
            self.stockOrder("milk chocolate", 5)
        if whitecounter < 2:
            self.stockOrder("white chocolate", 5)
        if blackcounter < 2:
            self.stockOrder("black chocolate", 5)
        if browncounter < 2:
            self.stockOrder("brown chocolate", 5)

        #HoneyStock
        length = self.honeystock.getLength()
        if length < 2:
            self.stockOrder("honey", 5)

        #MarshmallowStock
        length = self.marshmallowstock.getLength()
        if length < 2:
            self.stockOrder("marshmallow", 5)

        #ChilipepperStock
        length = self.chilipepperstock.getLength()
        if length < 2:
            self.stockOrder("chilipepper", 5)

        return True
            
"""
        >>> t = StockTable()
        >>> h = Honey(5)
        >>> h2 = Honey(2)
        >>> t.tableInsert(h)
        True
        >>> t.tableInsert(h2)
        True
        >>> t.tableInsert(h2)
        True
        >>> s = Stock()
        >>> s.stockCheck()
True
"""

t = StockTable()
c = ChocolateShot("milk chocolate", 5)
c3 = ChocolateShot("milk chocolate", 5)
c4 = ChocolateShot("milk chocolate", 5)
c2 = ChocolateShot("brown chocolate", 5)

t.tableInsert(c)
t.tableInsert(c2)
t.tableInsert(c3)
t.tableInsert(c4)

s = Stock()
s.setChocolatestock(t)
s.stockCheck()
