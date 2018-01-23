from Hashmap import Hashmap
from Hashmap import MapObject

class HMTable:  # Wrapper with table operations for Hashmap
    #Constructor
    def __init__(self, myType, max_size):
        self.hm = Hashmap(myType, max_size)

    #Deletes the hashmap
    def __del__(self):
        self.hm = None

    #Returns True if the Hashmap is empty
    def isEmpty(self):
        return self.hm.isEmpty()

    #Returns the length of the Hashmap
    def getLength(self):
        return self.hm.getLength()

    #Insert 'order' in the Hashmap
    #Returns True if succesful
    def tableInsert(self, order):
        return self.hm.insert(MapObject(order.getTimestamp(), order))

    #Deletes object from the Hashmap with 'timestamp'
    #Returns True if succesful
    def tableDelete(self, timestamp):
        return self.hm.erase(timestamp)
    
    #Returns the elements of the Hashmap as a list
    def traverseTable(self):
        return self.hm.traverse()
