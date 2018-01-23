from TwoThreeFourTree import TwoThreeFourTree
from TreeItem import TreeItem

class TTFTTable:    # Wrapper with table operations for TwoThreeFourTree
    #Constructor
    #Creates TwoThreeFourTree
    def __init__(self):
        self.ttft = TwoThreeFourTree()

    #Destructor, deletes the tree
    def __del__(self):
        self.ttft = None

    #Returns True if tree is empty
    def isEmpty(self):
        return self.ttft.isEmpty()

    #Returns the length of the tree
    def getLength(self):
        return self.ttft.getTreeLength()

    #Inserts an order in the tree
    #:param order: Order to add
    #:return bool: True if succesful
    def tableInsert(self, order):
        return self.ttft.twoThreeFourTreeInsert(TreeItem(order, order.getTimestamp()))

    #Deletes an order from the three
    #:param timestamp: Timestamp of order to delete
    #:return bool: True if succesful
    def tableDelete(self, timestamp):
        return self.ttft.twoThreeFourTreeDelete(timestamp)

    #Returns a list of all the elements in the tree
    def traverseTable(self):
        return self.ttft.inorderTraverse()
