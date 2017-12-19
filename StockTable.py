from CircularLinkedList import CircularLinkedList
from Honey import Honey

class StockTable:
    def __init__(self): #Constructor
        self.list = CircularLinkedList()

    def __del__(self):  #Destructor
        self.list = None

    def isEmpty(self):  #Retrieves if table is empty
        return self.list.isEmpty()

    def getLength(self):    #Retrieves length of table
        return self.list.getLength()

    def tableInsert(self, newitem): #Inserts given item in table
        self.list.insert(0, newitem)
        self.sortTable()
        return True

    def tableDelete(self, expiredate):  #Deletes ingredient with given expiredate from table
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

    def tableDeleteOldest(self):
        self.list.delete(0)

    def tableDeleteOldestShot(self, type):
        found = False
        count = 0
        while not found:
            if self.list.retrieve(count)[0].getType() == type:
                self.list.delete(count)
                found = True
            else:
                count += 1

    def tableRetrieve(self, expiredate): #Retrieves ingredient with given expiredate from table
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

    def traverseTable(self):    #Traverses table on ascending expiredate
        traverseList = []
        for i in range(0, self.getLength()):
            traverseList.append(self.list.retrieve(i)[0])
        return traverseList

    def sortTable(self):    #Sort table on ascending expiredate
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

    def print(self):    #Function for testing purposes: prints traverseTable
        t = self.traverseTable()
        for i in t:
            print(i.getExpiredate())
