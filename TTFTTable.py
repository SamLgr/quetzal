from TwoThreeFourTree import TwoThreeFourTree

class TTFTTable:
    def __init__(self):
        self.ttft = TwoThreeFourTree()

    def __del__(self):
        self.ttft = None

    def isEmpty(self):
        return self.ttft.isEmpty()

    def getLength(self):
        return self.ttft.getTreeLength()

    def tableInsert(self, newitem):
        return self.ttft.twoThreeFourTreeInsert(newitem)

    def tableDelete(self, timestamp):
        return self.ttft.twoThreeFourTreeDelete(timestamp)

    def traverseTable(self):
        return self.ttft.inorderTraverse()

    def print(self):
        return self.ttft.print()