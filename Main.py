#
# Created by Lander De Roeck on 19/12/17
#

import csv

from Stock import Stock
from StockTable import StockTable
from ChocolateShot import ChocolateShot
from ChocolateMilk import ChocolateMilk
from Honey import Honey
from Marshmallow import Marshmallow
from ChiliPepper import ChiliPepper
from Worker import Worker
from User import User

from Order import Order
from Queue import Queue

# init empty stocks for ingredients
chocolatestock = StockTable()
honeystock = StockTable()
marshmallowstock = StockTable()
chilipepperstock = StockTable()
# add stocks to stock
ingredients_stock = Stock(chocolatestock, honeystock, marshmallowstock, chilipepperstock)
# init workers
workers = []
# init users
users = []
# init orders
orders = Queue()
# init idcounter
chocolateid = 0


def createLogInfo(timestamp):
    # Backs up relevant info
    pass

def createLogFile(timestamp):
    # Creates log file in HTML standard
    pass


def findUser(email):
    for i in users:
        if i.getMailadress() == email:
            return i.getId()
    return None


def availableWorker():
    for w in workers:  # deze range wil ik graag bij volgende versie veranderen naar werker zoeken met hoogste werkload eerst.
        if w.occupied == False:
            return w
    return False


def executeOrder(order):  # 66
    if availableWorker():
        currentWorker = availableWorker()
        currentWorker.setOccupied()
        currentWorker.order = order;

        #Als chocobestelling meer workload in neemt dan werknemer aankan
        if order.chocoid.workload > currentWorker.workload and order.currworker is None:
            #Sla worker op in order
            order.currworker = currentWorker
  
        #Als chocobestelling minder of evenveel workload in neemt dan werknemer aankan
        elif order.chocoid.workload <= currentWorker.workload and order.currworker is None:
            #Chocolade workload is helemaal weg gedaan door de workload van de werknemer
            order.chocoid.workload = 0
            #Sla worked op in order
            order.currworker = currentWorker

        elif order.currworker != None:
            #order.chocoid.workload -= currentWorker.workload
            return False

        return True


def makeChoco(arguments):
    global chocolateid
    chocolateid += 1
    choco = ChocolateMilk(chocolateid)
    for ingredient in arguments:
        if ingredient == "melk":
            choco.addIngredient(ChocolateShot("milk", "unimportant"))
            ingredients_stock.stockDelete("milk chocolate")
        elif ingredient == "wit":
            choco.addIngredient(ChocolateShot("white", "unimportant"))
            ingredients_stock.stockDelete("white chocolate")
        elif ingredient == "bruin":
            choco.addIngredient(ChocolateShot("brown", "unimportant"))
            ingredients_stock.stockDelete("brown chocolate")
        elif ingredient == "zwart":
            choco.addIngredient(ChocolateShot("black", "unimportant"))
            ingredients_stock.stockDelete("black chocolate")
        elif ingredient == "chili":
            choco.addIngredient(ChiliPepper("unimportant"))
            ingredients_stock.stockDelete("chilipepper")
        elif ingredient == "marshmallow":
            choco.addIngredient(Marshmallow("unimportant"))
            ingredients_stock.stockDelete("marshmallow")
        elif ingredient == "honing":
            choco.addIngredient(Honey("unimportant"))
            ingredients_stock.stockDelete("honey")
    return chocolateid


# Function to delete worker
# param id: ID of the worker to delete
def delWorker(id):
    for worker in workers:
        if worker.id == id:
            del worker
            return True
    return False


def init_command(command):
    if command[0] == "shot":
        if len(command) == 6:
            for _ in range(int(command[2])):
                expiredate = ''.join(command[4:])
                chocolate = ChocolateShot(command[1], expiredate)
                chocolatestock.tableInsert(chocolate)
    elif command[0] == "honing":
        if len(command) == 5:
            for _ in range(int(command[1])):
                expiredate = ''.join(command[3:])
                honing = Honey(expiredate)
                honeystock.tableInsert(honing)
    elif command[0] == "marshmallow":
        if len(command) == 5:
            for _ in range(int(command[1])):
                expiredate = ''.join(command[3:])
                marshmallow = Marshmallow(expiredate)
                marshmallowstock.tableInsert(marshmallow)
    elif command[0] == "chili":
        if len(command) == 5:
            for _ in range(int(command[1])):
                expiredate = ''.join(command[3:])
                chili = ChiliPepper(expiredate)
                chilipepperstock.tableInsert(chili)
    elif command[0] == "gebruiker":
        if len(command) == 4:
            userid = len(users)
            user = User(userid, command[1], command[2], command[3])
            users.append(user)
    elif command[0] == "werknemer":
        if len(command) == 4:
            workerid = len(workers)
            worker = Worker(workerid, command[1], command[2], command[3])
            workers.append(worker)


def execute_command(command):
    if command[1] == "bestel":
        userid = findUser(command[2])
        chocoid = makeChoco(command[3:])
        order = Order(userid, command[0], chocoid, False)
        orders.enqueue(order)
    elif command[1] == "stock":
        init_command(command[2:])
    elif command[1] == "log":
        createLogFile(command[0])


def readfile(filename):  # returns array of arrays with input
    with open(filename, 'r') as FileIn:
        file_input = [rij for rij in csv.reader(FileIn, delimiter=' ')]

    init_enabled = True
    tijdstip = 0

    for command in file_input:
        if len(command) != 0 and command[0] != "#":
            if command[0] == "start":
                init_enabled = False
            if init_enabled:
                init_command(command)
            else:
                # Backs up relevant info for log file
                if command[0] != "start" and int(command[0]) > tijdstip:
                    createLogInfo(tijdstip)
                    tijdstip = int(command[0])
                execute_command(command)


readfile('system.txt')
print(delWorker(1))
print(delWorker(5))
