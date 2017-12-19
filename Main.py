#
# Created by Lander De Roeck on 19/12/17
#

import csv

from Stock import Stock
from StockTable import StockTable
from ChocolateShot import ChocolateShot
from Honey import Honey
from Marshmallow import Marshmallow
from ChiliPepper import ChiliPepper
from Worker import Worker
from User import User

# init empty stocks for ingredients
chocolatestock = StockTable()
honeystock = StockTable()
marshmallowstock = StockTable()
chilipepperstock = StockTable()
# init workers
workers = []
# init users
users = []


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
            users.append(worker)


def execute_command(command):
    # add stocks to stock
    ingredients_stock = Stock(chocolatestock, honeystock, marshmallowstock, chilipepperstock)


    pass


def readfile(filename):  # returns array of arrays with input
    with open(filename, 'r') as FileIn:
        file_input = [rij for rij in csv.reader(FileIn, delimiter=' ')]

    init_enabled = True

    for command in file_input:
        if len(command) != 0 and command[0] != "#":
            if command[0] == "start":
                init_enabled = False
            if init_enabled:
                init_command(command)
            else:
                execute_command(command)


readfile('system.txt')
