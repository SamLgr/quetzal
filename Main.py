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
# init orders (renamed queue to avoid overriding from internal defined queue)
orders = ourQueue()
# list for orders that are currently being worked on
current_orders = []
# init idcounter
chocolateid = 0
# init tijdstip
tijdstip = 0
# init loginfo
loginfo = []
# chocolates
chocolates = Hashmap(1, 200)


def jumpTime():
    for order in current_orders:
        choco = chocolates.retrieve(order.chocolateid)
        if choco.workload <= order.currworker.workload:
            choco.workload = 0
            order.currworker.setOccupied(False)
            current_orders.remove(order)
        else:
            choco.workload -= order.currworker.workload
    while availableWorker() and not orders.isEmpty():
        executeOrder(orders.dequeue()[0])
    createLogInfo()


def createLogInfo(timestamp=-1):
    if (timestamp >= 0 and timestamp < len(loginfo)):
        currentorders = deepcopy(orders)
        currentingredients = deepcopy(ingredients_stock)
        currenthandledorders = deepcopy(current_orders)
        currentchocolates = deepcopy(chocolates)
        loginfo[timestamp][0] = currentorders  # Logs current queue
        loginfo[timestamp][1] = currentingredients  # Logs current stock
        loginfo[timestamp][2] = currenthandledorders  # Logs current orders that are being worked on
        loginfo[timestamp][3] = currentchocolates  # Logs current chocolates
    else:
        loginfo.append([])
        currentorders = deepcopy(orders)
        currentingredients = deepcopy(ingredients_stock)
        currenthandledorders = deepcopy(current_orders)
        currentchocolates = deepcopy(chocolates)
        loginfo[len(loginfo) - 1].append(currentorders)  # Logs current queue
        loginfo[len(loginfo) - 1].append(currentingredients)  # Logs current stock
        loginfo[len(loginfo) - 1].append(currenthandledorders)  # Logs current orders that are being worked on
        loginfo[len(loginfo) - 1].append(currentchocolates)  # Logs current chocolates


def createLogFile(timestamp):
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
    for worker in workers:
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
    for timestamp in range(0, len(loginfo)):
        htmlfile.write("<tr>")
        htmlfile.write("<td>")
        htmlfile.write(str(timestamp))
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str("#TODO"))    #TODO: write stack info (need stack)
        htmlfile.write("</td>")
        for worker in workers:
            htmlfile.write("<td>")
            for order in loginfo[timestamp][2]:
                if order.currworker.getId() == worker.getId():
                    htmlfile.write(str(loginfo[timestamp][3].retrieve(order.getChocolateid()).returnWorkload()))
            htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str("#TODO"))    #TODO: write new orders (need ordertable)
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(loginfo[timestamp][0].traverse()))
        htmlfile.write("</td>")
        chocstock = loginfo[timestamp][1].getChocolatestock()
        hstock = loginfo[timestamp][1].getHoneystock()
        mstock = loginfo[timestamp][1].getMarshmallowstock()
        chilistock = loginfo[timestamp][1].getChilipepperstock()
        htmlfile.write("<td>")
        htmlfile.write(str(chocstock.getShotLength("white")))
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(chocstock.getShotLength("milk")))
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(chocstock.getShotLength("brown")))
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(chocstock.getShotLength("black")))
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(hstock.getLength()))
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(mstock.getLength()))
        htmlfile.write("</td>")
        htmlfile.write("<td>")
        htmlfile.write(str(chilistock.getLength()))
        htmlfile.write("</td>")
        htmlfile.write("</tr>")

    htmlstr = """
                </tbody>
                </table>
            </body>
        </html>
    """
    htmlfile.write(htmlstr)


def findUser(email):
    for i in users:
        if i.getMailadress() == email:
            return i.getId()
    return None


#Used in:
# - avaiableWorker()
def selection_sort(l):
    for i in range(0, len(l) -1):
        indexOfSmallest = i
        for j in range(i + 1, len(l)):
            if l[j].getWorkload() > l[indexOfSmallest].getWorkload():
                indexOfSmallest = j
        if indexOfSmallest != i:
            l[i], l[indexOfSmallest] = l[indexOfSmallest], l[i]
    
    return l

def availableWorker():
    sortedWorkers = selection_sort(workers) 
    for w in sortedWorkers:
        if w.occupied == False:
            return w
    return False


def executeOrder(order):  # 66
    current_orders.append(order)
    choco = chocolates.retrieve(order.chocolateid)
    for i in range(choco.ingredients.getLength()):
        ingredient = choco.ingredients.retrieve(i)[0]
        if type(ingredient) is ChocolateShot:
            chocolatetype = ingredient.type + " chocolate"
            ingredients_stock.stockDelete(chocolatetype)
        elif type(ingredient) is Honey:
            ingredients_stock.stockDelete("honey")
        elif type(ingredient) is ChiliPepper:
            ingredients_stock.stockDelete("chilipepper")
        elif type(ingredient) is Marshmallow:
            ingredients_stock.stockDelete("marshmallow")
        else:
            print(type(ingredient))
    currentWorker = availableWorker()
    currentWorker.setOccupied(True)
    currentWorker.order = order
    order.currworker = currentWorker



def makeChoco(arguments):
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
    for worker in workers:
        if worker.id == workerid:
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
                print(command)
                # Backs up relevant info for log file
                if command[0] != "start" and int(command[0]) > tijdstip:
                    jumpTime()
                    tijdstip = int(command[0])
                execute_command(command)


readfile('system.txt')
print(delWorker(1))
print(delWorker(5))
