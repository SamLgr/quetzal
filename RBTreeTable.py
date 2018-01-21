from RBTree import redBlackTree, TreeItem

class RBTTable:
    def __init__(self):
        self.rbt = redBlackTree()

    def __del__(self):
        self.rbt = None

    def isEmpty(self):
        return self.rbt.isEmtpy()

    def getLength(self):
        return self.rbt.getLength()

    def tableInsert(self, order):
        return self.rbt.insertItem(TreeItem(order, order.getTimestamp()))

    def tableDelete(self, key):
        return self.rbt.deleteItem(key)

    def traverseTable(self):
        return self.rbt.inorderTraverse()
