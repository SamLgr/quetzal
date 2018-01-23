#
# Made by Lander De Roeck on 13/11/17
#

class Node(object):
    #Constructor
    #:param item: set initial value
    #:param next: Pointer to next Node
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
    
    #Returns the value of this node
    def getItem(self):
        return self.item

    #Sets value of this node
    def setItem(self, item):
        self.item = item

    #Set pointer to next node in the list
    def setNext(self, next):
        self.next = next
    
    #Returns node after the current one
    def getNext(self):
        return self.next


class doubleNode(object):
    
    #Constructor
    #:param item: Initial value to set
    #:param prev: Previous node in the list
    #:param next: Next node in the list
    def __init__(self, item, prev=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

    #Returns if this node has value 'value'
    #:param value: Value to check
    #:return bool: Returns True if values match
    def has_value(self, value):
        return self.item == value

    #Sets pointer to next Node in the list
    def setNext(self, next):
        self.next = next

    #Sets pointer to previous Node in the list
    def setPrev(self, prev):
        self.prev = prev

    #Returns the value of this Node
    def getItem(self):
        return self.item

    #Sets the value of this Node to 'item'
    def setItem(self, item):
        self.item = item

    #Returns next Node in the list
    def getNext(self):
        return self.next

    #Returns previous Node in the list
    def getPrev(self):
        return self.prev
