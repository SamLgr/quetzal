from BinarySearchTree import BinarySearchTree
from TreeItem import TreeItem

class BSTTable:     # Wrapper with table operations for BinarySearchTree
    def __init__(self):
        self.bst = BinarySearchTree()

    def __del__(self):
        self.bst = None

    def isEmpty(self):
        return self.bst.isEmpty()

    def getLength(self):
        return self.bst.getTreeLength()

    def tableInsert(self, order):
        return self.bst.searchTreeInsert(TreeItem(order, order.getTimestamp()))

    def tableDelete(self, timestamp):
        return self.bst.searchTreeDelete(timestamp)

    def traverseTable(self):
        return self.bst.inorderTraverse()