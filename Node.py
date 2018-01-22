class Node():
    # Constructor
    # item: item to be added to ADT
    # next: pointer to next item in ADT, automatically initialises to None if no parameter is given
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

    # Returns item in node
    def getItem(self):
        return self.item

    # Returns pointer to next node
    def getNext(self):
        return self.next

    # Sets pointer to next node to given pointer
    def setNext(self, next):
        self.next = next
