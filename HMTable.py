from Hashmap import Hashmap
from Hashmap import MapObject

class HMTable:  # Wrapper with table operations for Hashmap
    def __init__(self):
        self.hm = Hashmap()

    def __del__(self):
        self.hm = None

    def isEmpty(self):
        return self.hm.isEmpty()

    def getLength(self):
        return self.hm.getLength()

    def tableInsert(self, order):
        return self.hm.insert(MapObject(order.getTimestamp(), order))

    def tableDelete(self, timestamp):
        return self.hm.erase(timestamp)

    def traverseTable(self):
        return self.hm.traverse()
