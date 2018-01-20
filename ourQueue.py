#
# Made by Lander De Roeck on 13/11/17
#


"""
Testing queue
>>> q = Queue()
>>> q.isEmpty()
True
>>> q.enqueue("A")
>>> q.enqueue("B")
>>> q.enqueue("C")
>>> q.isEmpty()
False
>>> q.getLength()
3
>>> q.getFront()
('A', True)
>>> q.dequeue()
('A', True)
>>> q.getLength()
2
>>> q.dequeue()
('B', True)
>>> q.getLength()
1
>>> q.dequeue()
('C', True)
>>> q.dequeue()
(None, False)
>>> q.getLength()
0
"""

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

    def traverse(self):
        """
        >>> q = Queue()
        >>> q.enqueue("A")
        >>> q.enqueue("B")
        >>> q.enqueue("C")
        >>> q.traverse()
        ['A', 'B', 'C']
        """
        buffer = []
        current = self.frontPtr
        if current is None:
            return buffer

        buffer.append(current.item)
        while current.getNext():
            current = current.getNext()
            buffer.append(current.item)
        return buffer

    def getLength(self):
        current = self.frontPtr
        if current is None: return 0

        sum = 1
        while (current.getNext()):
            sum += 1
            current = current.getNext()

        return sum

