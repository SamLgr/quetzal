from CircularLinkedList import CircularLinkedList
from Honey import Honey

class StockTable:
    # Constructor
    # list: List containing ingredients
    def __init__(self):
        self.list = CircularLinkedList()

    # Destructor
    def __del__(self):
        self.list = None

    # Returns if stock table is empty
    def isEmpty(self):
        return self.list.isEmpty()

    # Returns length of stock table
    def getLength(self):
        return self.list.getLength()

    # Returns amount of shots in stock table with given types
    def getShotLength(self, type):
        count = 0
        for i in range(0, self.getLength()):
            if self.list.retrieve(i)[0].getType() == type:
                count += 1
        return count

    # Inserts given item in stock table
    def tableInsert(self, newitem):
        self.list.insert(0, newitem)
        self.sortTable()
        return True

    # Deletes ingredient with given expire date from stock table
    def tableDelete(self, expiredate):
        first = 0
        last = self.getLength() - 1
        found = False
        while first <= last and not found:
            mid = (first + last)//2
            current = self.list.retrieve(mid)[0]
            if current.getExpiredate() == expiredate:
                self.list.delete(mid)
                found = True
            else:
                if expiredate < current.getExpiredate():
                    last = mid - 1
                else:
                    first = mid + 1
        return found

    # Deletes oldest ingredient from stock table
    def tableDeleteOldest(self):
        self.list.delete(0)

    # Deletes oldest shot with given type from stock table
    def tableDeleteOldestShot(self, type):
        found = False
        count = 0
        while not found:
            if self.list.retrieve(count)[0].getType() == type:
                self.list.delete(count)
                found = True
            else:
                count += 1

    # Retrieves ingredient with given expire date from stock table
    def tableRetrieve(self, expiredate):
        first = 0
        last = self.getLength() - 1
        found = False
        while first <= last and not found:
            mid = (first + last) // 2
            current = self.list.retrieve(mid)[0]
            if current.getExpiredate() == expiredate:
                return current, True
            else:
                if expiredate < current.getExpiredate():
                    last = mid - 1
                else:
                    first = mid + 1
        return None, False

    # Traverses stock table on ascending expire date
    def traverseTable(self):
        return self.list.getItems()

    # Sorts stock table on ascending expire date
    def sortTable(self):
        """
        >>> t = StockTable()
        >>> h = Honey(5)
        >>> h2 = Honey(2)
        >>> t.tableInsert(h)
        True
        >>> t.tableInsert(h2)
        True
        >>> t.tableDelete(2)
        True
        >>> t.tableInsert(h2)
        True
        >>> t.tableRetrieve(5)
        >>> t.traverseTable()
        >>> t.sortTable()
        >>> t.print()
        """
        swap = True
        while swap:
            swap = False
            for i in range(0, self.list.getLength()-1):
                current = self.list.retrieve(i)[0]
                if current.getExpiredate() > self.list.retrieve(i + 1)[0].getExpiredate():
                    self.list.delete(i)
                    self.list.insert(i + 1, current)
                    swap = True

    # Function for testing purposes: prints traverseTable
    def print(self):
        t = self.traverseTable()
        for i in t:
            print(i.getExpiredate())
