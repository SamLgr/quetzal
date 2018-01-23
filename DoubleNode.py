#
# Made by Lander De Roeck on 13/11/17
#

class Node(object):
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def getItem(self):
        return self.item

    def setItem(self, item):
        self.item = item

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

class doubleNode(object):
    def __init__(self, item, prev=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

    def has_value(self, value):
        return self.item == value

    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def getItem(self):
        return self.item

    def setItem(self, item):
        self.item = item

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev
