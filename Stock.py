from StockTable import StockTable
from ChocolateShot import ChocolateShot
from Honey import Honey
from Marshmallow import Marshmallow
from ChiliPepper import ChiliPepper

class Stock:
    def __init__(self, chocolatestock=StockTable(), honeystock=StockTable(), marshmallowstock=StockTable(), chilipepperstock=StockTable()):
        self.chocolatestock = chocolatestock
        self.honeystock = honeystock
        self.marshmallowstock = marshmallowstock
        self.chilipepperstock = chilipepperstock

    def __del__(self):
        self.chocolatestock = None
        self.honeystock = None
        self.marshmallowstock = None
        self.chilipepperstock = None

    def getChocolatestock(self):
        return self.chocolatestock

    def getHoneystock(self):
        return self.honeystock

    def getMarshmallowstock(self):
        return self.marshmallowstock

    def getChilipepperstock(self):
        return self.chilipepperstock

    def setChocolatestock(self, chocolatestock):
        self.chocolatestock = chocolatestock

    def setHoneystock(self, honeystock):
        self.honeystock = honeystock

    def setMarshmallowstock(self, marshmallowstock):
        self.marshmallowstock = marshmallowstock

    def setChilipepperstock(self, chilipepperstock):
        self.chilipepperstock = chilipepperstock

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

    def stockOrder(self, stockType, amount):
        if stockType == "white chocolate":
            while amount != 0:
                chocolate = ChocolateShot("white")
                self.chocolatestock.tableInsert(chocolate)
        elif stockType == "milk chocolate":
            while amount != 0:
                chocolate = ChocolateShot("milk")
                self.chocolatestock.tableInsert(chocolate)
        elif stockType == "brown chocolate":
            while amount != 0:
                chocolate = ChocolateShot("brown")
                self.chocolatestock.tableInsert(chocolate)
        elif stockType == "black chocolate":
            while amount != 0:
                chocolate = ChocolateShot("black")
                self.chocolatestock.tableInsert(chocolate)
        elif stockType == "honey":
            while amount != 0:
                honey = Honey()
                self.honeystock.tableInsert(honey)
        elif stockType == "marshmallow":
            while amount != 0:
                marshmallow = Marshmallow()
                self.marshmallowstock.tableInsert(marshmallow)
        elif stockType == "chilipepper":
            while amount != 0:
                chilipepper = ChiliPepper()
                self.chilipepperstock.tableInsert(chilipepper)