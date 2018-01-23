from RBTree import redBlackTree, TreeItem

class RBTTable:     # Wrapper with table operations for RBTree
    #Constructor, created a RBTree
    def __init__(self):
        self.rbt = redBlackTree()

    #Destructor, deleted the RBTree
    def __del__(self):
        self.rbt = None

    #Returns True if RBTree is empty
    def isEmpty(self):
        return self.rbt.isEmtpy()

    #Returns the amount of elements in the RBTreee
    def getLength(self):
        return self.rbt.getLength()

    #Inserts an order in the RBTree
    #:param order: Order to add
    #:return bool: Returns True if succesful
    def tableInsert(self, order):
        return self.rbt.insertItem(TreeItem(order, order.getTimestamp()))
    
    #Deletes the order 
    #:param key: Key of order in RBTree to delete
    #:return bool: Returns True if succesful
    def tableDelete(self, key):
        return self.rbt.deleteItem(key)

    #Returns a list of all orders in the RBTree
    def traverseTable(self):
        return self.rbt.inorderTraverse()
