#
# Created by Lander De Roeck on 19/12/17
#

import csv
from copy import deepcopy

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
from ourQueue import Queue as ourQueue
from Hashmap import Hashmap, MapObject
from Stack import Stack
from BSTTable import BSTTable
from TTFTTable import TTFTTable
from RBTreeTable import RBTTable
from HMTable import HMTable
from DoubleList import DoubleList
from CircularLinkedList import CircularLinkedList

# init empty stocks for ingredients
chocolatestock = StockTable()
honeystock = StockTable()
marshmallowstock = StockTable()
chilipepperstock = StockTable()
# add stocks to stock
ingredients_stock = Stock(chocolatestock, honeystock, marshmallowstock, chilipepperstock)
# init workers
workers = DoubleList()
#
workerstack = Stack()
# init users
users = DoubleList()
# init orders (renamed queue to avoid overriding from internal defined queue)
orders = ourQueue()
# list for orders that are currently being worked on
current_orders = []
# processed orders
processed_orders = HMTable(1, 500)
# init idcounter
chocolateid = 0
# init tijdstip
tijdstip = 0
# init loginfo
loginfo = []
# chocolates
chocolates = Hashmap(1, 200)


def jumpTime():
    # handles passage timestamp
    global current_orders
    passthrough = []
    for order in current_orders:
        choco = chocolates.retrieve(order.chocolateid)
        if choco.workload <= order.currworker.workload:
            choco.workload = 0
            order.currworker.setOccupied(False)
            workerstack.push(order.currworker)
            order.setCollected(True)
            processed_orders.tableInsert(order)
        else:
            choco.workload -= order.currworker.workload
            passthrough.append(order)
    current_orders = passthrough
    while not workerstack.isEmpty() and not orders.isEmpty():
        executeOrder(orders.dequeue()[0])
    createLogInfo()


def createLogInfo():    # Logs info into loginfo list for every timestamp (uses deepcopy)
    loginfo.append([])
    currentorderque = deepcopy(orders)
    currentingredients = deepcopy(ingredients_stock)
    currenthandledorders = deepcopy(current_orders)
    currentchocolates = deepcopy(chocolates)
    currentstack = deepcopy(workerstack)
    loginfo[len(loginfo) - 1].append(currentorderque)  # Logs current queue
    loginfo[len(loginfo) - 1].append(currentingredients)  # Logs current stock
    loginfo[len(loginfo) - 1].append(currenthandledorders)  # Logs current orders that are being worked on
    loginfo[len(loginfo) - 1].append(currentchocolates)  # Logs current chocolates
    loginfo[len(loginfo) - 1].append(currentstack)  # Logs current worker stacks


def createLogFile(timestamp):   # Creates a log file based on loginfo
    htmlstr = """
    	<html>
    		<head>
    		<style>
    			table {
    			    border-collapse: collapse;
    			}

    			table, td, th {
    			    border: 1px solid black;
    			}
    		</style>
    	</head>
    		<body>
    			<h1>Log</h1>
    			<table>
    				<thead>
    					<td>tijdstip</td>
    					<td>Stack</td>
    	"""

    htmlfile = open('log' + timestamp + '.html', 'w+')
    htmlfile.write(htmlstr)
    for worker in workers.traverse():  # Write one column per worker
        htmlfile.write("<td>")
        htmlfile.write(worker.getName()[0] + " " + worker.getName()[1])
        htmlfile.write("</td>")

    htmlstr = """
    			        <td>Nieuwe bestellingen</td> 
				        <td>Wachtende bestellingen</td>
				        <td>wit</td>
				        <td>melk</td>
				        <td>bruin</td>
				        <td>zwart</td>
				        <td>honing</td>
				        <td>marshmallow</td>
				        <td>chili</td>
			        </thead>
			        <tbody>
    """
    htmlfile.write(htmlstr)
    for timestamp in range(0, len(loginfo)):    # Write info for every timestamp
        currentorderque = loginfo[timestamp][0]   # Get data from loginfo
        currentingredients = loginfo[timestamp][1]
        currenthandledorders = loginfo[timestamp][2]
        currentchocolates = loginfo[timestamp][3]
        currentstack = loginfo[timestamp][4]
        currentneworders = []
        for order in currenthandledorders:
            if order.getTimestamp() == timestamp:
                currentneworders.append(order)
        for order in currentorderque.traverse():
            if order.getTimestamp() == timestamp:
                currentneworders.append(order)
        htmlfile.write("<tr>")
        htmlfile.write("<td>")
        htmlfile.write(str(timestamp))  # Write current timestamp
        htmlfile.write("</td>")
        htmlfile.write("<td>| ")
        htmlfile.write(" ".join(str(worker.getWorkload()) for worker in currentstack.traverse()))   # Write stack with workloads at timestamp
        htmlfile.write("</td>")
        for worker in workers.traverse():
            htmlfile.write("<td>")
            for order in currenthandledorders:
                if order.currworker.getId() == worker.getId():
                    htmlfile.write(str(currentchocolates.retrieve(order.getChocolateid()).getWorkload()))    # Write remaining workload for order being handled by worker
            htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(", ".join(str(currentchocolates.retrieve(order.getChocolateid()).getWorkload()) for order in currentneworders))     # Write workloads of new orders incoming at timestamp
        htmlfile.truncate()
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(", ".join(str(currentchocolates.retrieve(order.getChocolateid()).getWorkload()) for order in currentorderque.traverse()))   # Write workloads of orders in queue at timestamp
        htmlfile.write("</td>")
        chocstock = currentingredients.getChocolatestock()  # Get stocks from StockTable
        hstock = currentingredients.getHoneystock()
        mstock = currentingredients.getMarshmallowstock()
        chilistock = currentingredients.getChilipepperstock()
        types = ["white", "milk", "brown", "black"]
        for choctype in types:
            htmlfile.write("<td>")
            htmlfile.write(str(chocstock.getShotLength(choctype)))  # Write amount of white, milk, brown and black chocolate shots in stock
            htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(hstock.getLength()))     # Write amount of honey in stock
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(mstock.getLength()))     # Write amount of marshmallows in stock
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(chilistock.getLength()))     # Write amount of chilipeppers in stock
        htmlfile.write("</td>")
        htmlfile.write("</tr>")

    htmlstr = """
                </tbody>
                </table>
            </body>
        </html>
    """
    htmlfile.write(htmlstr)     # End HTML body
    print("Processed orders:")
    for order in processed_orders.traverseTable():
        print("Order with ID: " + str(order.getChocolateid()))


def findUser(email):
    list_users = users.traverse()
    for i in list_users:
        if i.getMailadress() == email:
            return i.getId()
    return None


# #Used in:
# # - avaiableWorker()
# def selection_sort(l):
#     for i in range(0, len(l) -1):
#         indexOfSmallest = i
#         for j in range(i + 1, len(l)):
#             if l[j].getWorkload() > l[indexOfSmallest].getWorkload():
#                 indexOfSmallest = j
#         if indexOfSmallest != i:
#             l[i], l[indexOfSmallest] = l[indexOfSmallest], l[i]
#
#     return l
#
# def availableWorker():
#     sortedWorkers = selection_sort(workers)
#     for w in sortedWorkers:
#         if w.occupied == False:
#             return w
#     return False


def executeOrder(order):
    # links a available worker to order, removes ingredients from stock
    current_orders.append(order)
    choco = chocolates.retrieve(order.getChocolateid())
    for i in range(choco.getIngredients().getLength()):
        ingredient = choco.getIngredients().retrieve(i)[0]
        if type(ingredient) is ChocolateShot:
            chocolatetype = ingredient.getType() + " chocolate"
            ingredients_stock.stockDelete(chocolatetype)
        elif type(ingredient) is Honey:
            ingredients_stock.stockDelete("honey")
        elif type(ingredient) is ChiliPepper:
            ingredients_stock.stockDelete("chilipepper")
        elif type(ingredient) is Marshmallow:
            ingredients_stock.stockDelete("marshmallow")
        else:
            print(type(ingredient))
    currentWorker = workerstack.pop()[0]
    currentWorker.setOccupied(True)
    currentWorker.setOrder(order)
    order.setWorker(currentWorker)



def makeChoco(arguments):
    # creates ChocolateMilk which gets stored in hashmap on id, returns id
    global chocolateid
    chocolateid += 1
    choco = ChocolateMilk(chocolateid)
    for ingredient in arguments:
        if ingredient == "milk":
            choco.addIngredient(ChocolateShot("milk", 10**9))
            # ingredients_stock.stockDelete("milk chocolate")
        elif ingredient == "white":
            choco.addIngredient(ChocolateShot("white", 10**9))
            # ingredients_stock.stockDelete("white chocolate")
        elif ingredient == "brown":
            choco.addIngredient(ChocolateShot("brown", 10**9))
            # ingredients_stock.stockDelete("brown chocolate")
        elif ingredient == "black":
            choco.addIngredient(ChocolateShot("black", 10**9))
            # ingredients_stock.stockDelete("black chocolate")
        elif ingredient == "chili":
            choco.addIngredient(ChiliPepper(10**9))
            # ingredients_stock.stockDelete("chilipepper")
        elif ingredient == "marshmallow":
            choco.addIngredient(Marshmallow(10**9))
            # ingredients_stock.stockDelete("marshmallow")
        elif ingredient == "honing":
            choco.addIngredient(Honey(10**9))
            # ingredients_stock.stockDelete("honey")
    chocolates.insert(MapObject(chocolateid, choco))
    return chocolateid


# Function to delete worker
# param id: ID of the worker to delete
def delWorker(workerid):
    for worker in workers.traverse():
        if worker.getId() == workerid:
            del worker
            return True
    return False


def init_command(command):
    # handles the init stage of the input file
    # adding users/workers/stock
    if command[0] == "shot":
        if len(command) == 6 and chocolatestock.getShotLength(command[1]) < 20:
            for _ in range(int(command[2])):
                expiredate = ''.join(command[3:])
                chocolate = ChocolateShot(command[1], expiredate)
                chocolatestock.tableInsert(chocolate)
    elif command[0] == "honing":
        if len(command) == 5 and honeystock.getLength() < 20:
            for _ in range(int(command[1])):
                expiredate = ''.join(command[2:])
                honing = Honey(expiredate)
                honeystock.tableInsert(honing)
    elif command[0] == "marshmallow":
        if len(command) == 5 and marshmallowstock.getLength() < 20:
            for _ in range(int(command[1])):
                expiredate = ''.join(command[2:])
                marshmallow = Marshmallow(expiredate)
                marshmallowstock.tableInsert(marshmallow)
    elif command[0] == "chili" and chilipepperstock.getLength() < 20:
        if len(command) == 5:
            for _ in range(int(command[1])):
                expiredate = ''.join(command[2:])
                chili = ChiliPepper(expiredate)
                chilipepperstock.tableInsert(chili)
    elif command[0] == "gebruiker":
        if len(command) == 4:
            userid = users.getLength()
            user = User(userid, command[1], command[2], command[3])
            users.append(user)
    elif command[0] == "werknemer":
        if len(command) == 4:
            workerid = workers.getLength()
            worker = Worker(workerid, command[1], command[2], command[3])
            workers.append(worker)
            workerstack.push(worker)


def execute_command(command):
    # handles the other commands
    # orders/log
    global tijdstip
    if command[1] == "bestel":
        userid = findUser(command[2])
        chocoid = makeChoco(command[3:])
        order = Order(userid, command[0], chocoid, False)
        orders.enqueue(order)
    elif command[1] == "stock":
        init_command(command[2:])
    elif command[1] == "log":
        tijdstip += 1
        jumpTime()
        createLogFile(command[0])


def readfile(filename):  # returns array of arrays with input
    with open(filename, 'r') as FileIn:
        file_input = [rij for rij in csv.reader(FileIn, delimiter=' ')]

    init_enabled = True
    global tijdstip

    for command in file_input:
        if len(command) != 0 and command[0] != "#":
            if command[0] == "start":
                init_enabled = False
            elif init_enabled:
                init_command(command)
            else:
                # print(command)
                # Backs up relevant info for log file
                if command[0] != "start" and int(command[0]) > tijdstip:
                    jumpTime()
                    tijdstip = int(command[0])
                execute_command(command)


readfile('system.txt')
# print(delWorker(1))
# print(delWorker(5))
