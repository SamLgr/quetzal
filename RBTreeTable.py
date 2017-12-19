from RBTree import redBlackTree

class RBTTable:
    def __init__(self):
        self.rbt = redBlackTree()

    def __del__(self):
        self.rbt = None

    def isEmpty(self):
        return self.rbt.isEmtpy()

    def getLength(self):
        return None # not implemented

    def tableInsert(self, newitem):
        return self.rbt.insertItem(newitem)

    def tableDelete(self, timestamp):
        return self.rbt.deleteItem(timestamp)

    def traverseTable(self):
        return None # not implemented