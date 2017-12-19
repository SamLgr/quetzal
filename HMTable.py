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

    def tableInsert(self, newitem):
        return self.hm.insert(newitem, newitem.getTimestamp())

    def tableDelete(self, timestamp):
        return self.hm.erase(timestamp)

    def traverseTable(self):
        return None # not implemented