from TwoThreeFourTree import TwoThreeFourTree
from TreeItem import TreeItem

class TTFTTable:
    def __init__(self):
        self.ttft = TwoThreeFourTree()

    def __del__(self):
        self.ttft = None

    def isEmpty(self):
        return self.ttft.isEmpty()

    def getLength(self):
        return self.ttft.getTreeLength()

    def tableInsert(self, order):
        treeitem = TreeItem(order, order.getTimestamp())
        return self.ttft.twoThreeFourTreeInsert(treeitem)

    def tableDelete(self, timestamp):
        return self.ttft.twoThreeFourTreeDelete(timestamp)

    def traverseTable(self):
        return self.ttft.inorderTraverse()