from Hashmap import Hashmap

class HMTable:
    def __init__(self):
        self.hm = Hashmap()

    def __del__(self):
        self.hm = None

    def isEmpty(self):
        return None # not implemented

    def getLength(self):
        return None # not implemented

    def tableInsert(self, order):
        return self.hm.insert(order, order.getTimestamp())

    def tableDelete(self, timestamp):
        return self.hm.erase(timestamp)

    def traverseTable(self):
        return None # not implemented