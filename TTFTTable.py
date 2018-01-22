from TwoThreeFourTree import TwoThreeFourTree
from TreeItem import TreeItem

class TTFTTable:    # Wrapper with table operations for TwoThreeFourTree
    def __init__(self):
        self.ttft = TwoThreeFourTree()

    def __del__(self):
        self.ttft = None

    def isEmpty(self):
        return self.ttft.isEmpty()

    def getLength(self):
        return self.ttft.getTreeLength()

    def tableInsert(self, order):
        return self.ttft.twoThreeFourTreeInsert(TreeItem(order, order.getTimestamp()))

    def tableDelete(self, timestamp):
        return self.ttft.twoThreeFourTreeDelete(timestamp)

    def traverseTable(self):
        return self.ttft.inorderTraverse()