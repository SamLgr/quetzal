#
# Made by Lander De Roeck on 13/11/17
#

from DoubleNode import Node

class Queue(object):
    def __init__(self):  # creates queue with None values
        self.frontPtr = None
        self.backPtr = None

    def createQueue(self, value):
        self.enqueue(value)

    def destroyQueue(self):
        self.frontPtr = None
        self.backPtr = None

    def isEmpty(self):
        return self.frontPtr is None and self.backPtr is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():  # no data present
            self.frontPtr = new_node
            self.backPtr = self.frontPtr
        else:  # some nodes exists
            self.backPtr.setNext(new_node)
            self.backPtr = new_node

    def dequeue(self):
        if self.isEmpty():
            return None, False
        else:  # something in the queue
            item = self.frontPtr.getItem()
            right = self.frontPtr.getNext()
            if right is None: # nothing else queued
                self.frontPtr = None
                self.backPtr = None
            else:
                self.frontPtr = right
            return item, True

    def getFront(self):
        if self.isEmpty():
            return None, False
        return self.frontPtr.getItem(), True
