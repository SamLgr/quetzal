from BinarySearchTree import BinarySearchTree
from TreeItem import TreeItem

class BSTTable:
    def __init__(self):
        self.bst = BinarySearchTree()

    def __del__(self):
        self.bst = None

    def isEmpty(self):
        return self.bst.isEmpty()

    def getLength(self):
        return self.bst.getTreeLength()

    def tableInsert(self, order):
        treeitem = TreeItem(order, order.getTimestamp())
        return self.bst.searchTreeInsert(treeitem)

    def tableDelete(self, timestamp):
        return self.bst.searchTreeDelete(timestamp)

    def traverseTable(self):
        return self.bst.inorderTraverse()