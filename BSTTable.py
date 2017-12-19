from BinarySearchTree import BinarySearchTree

class BSTTable:
    def __init__(self):
        self.bst = BinarySearchTree()

    def __del__(self):
        self.bst = None

    def isEmpty(self):
        return self.bst.isEmpty()

    def getLength(self):
        return self.bst.getTreeLength()

    def tableInsert(self, newitem):
        return self.bst.searchTreeInsert(newitem)

    def tableDelete(self, timestamp):
        return self.bst.searchTreeDelete(timestamp)

    def traverseTable(self):
        return self.bst.inorderTraverse()

    def print(self):
        return self.bst.print()