from Node import Node


class LinkedList:
    def __init__(self):
        """
        Initialiseert een lege gelinkte lijst

        >>> head = LinkedList().head
        >>> head.getItem() is None
        True
        """
        self.head = Node(None, None)
        self.head.setNext(None)

    def __del__(self):
        self.head = Node(None, None)
        self.head.setNext(None)

    def isEmpty(self):
        """
        Bepaalt of de gelinkte lijst leeg is
        :return: bool die aangeeft of de lijst leeg is

        >>> list = LinkedList()
        >>> list.isEmpty()
        True
        >>> list.insert(0, 5)
        True
        >>> list.isEmpty()
        False
        """
        return self.head.getNext() is None

    def getLength(self):
        """
        Bepaalt de lengte van de gelinkte lijst
        :return: lengte van de gelinkte lijst

        >>> list = LinkedList()
        >>> list.getLength()
        0
        >>> list.insert(0, 5)
        True
        >>> list.getLength()
        1
        >>> list.insert(1, 7)
        True
        >>> list.getLength()
        2
        """
        current = self.head.getNext()
        count = 0
        while current is not None:
            current = current.getNext()
            count += 1
        return count

    def insert(self, index, newItem):
        """
        Voegt element 'newItem' toe op positie 'index' in de gelinkte lijst.
        :param index: positie waar 'newItem' moet worden toegevoegd
        :param newItem: element dat moet worden toegevoegd
        :return: bool die aangeeft of het toevoegen gelukt is

        >>> list = LinkedList()
        >>> list.insert(1, 5)
        False
        >>> list.insert(0, 5)
        True
        >>> list.insert(1, 8)
        True
        >>> list.insert(1, 6)
        True
        >>> list.retrieve(0)
        (5, True)
        >>> list.retrieve(1)
        (6, True)
        >>> list.retrieve(2)
        (8, True)
        """
        if index > self.getLength() or index < 0:
            return False
        current = self.head
        for i in range(0, index + 1):
            previous = current
            current = current.getNext()
        node = Node(newItem, current)
        previous.setNext(node)
        return True

    def delete(self, index):
        """
        Verwijdert element op positie 'index' uit de gelinkte lijst.
        :param index: positie van element dat moet worden verwijderd
        :return: bool die aangeeft of het verwijderen gelukt is

        >>> list = LinkedList()
        >>> list.insert(1, 5)
        False
        >>> list.insert(0, 5)
        True
        >>> list.insert(1, 8)
        True
        >>> list.insert(1, 6)
        True
        >>> list.delete(1)
        True
        >>> list.retrieve(0)
        (5, True)
        >>> list.retrieve(1)
        (8, True)
        >>> list.delete(0)
        True
        >>> list.delete(1)
        False
        >>> list.delete(0)
        True
        >>> list.isEmpty()
        True

        """
        if index >= self.getLength() or index < 0:
            return False
        current = self.head
        for i in range(0, index + 1):
            previous = current
            current = current.getNext()
        previous.setNext(current.getNext())
        return True

    def retrieve(self, index):
        """
        Geeft element op positie 'index' in de gelinkte lijst terug.
        :param index: positie van het element
        :return: element op positie 'index', bool die aangeeft of het ophalen gelukt is

        >>> list = LinkedList()
        >>> list.insert(0, 5)
        True
        >>> list.insert(1, 8)
        True
        >>> list.insert(1, 6)
        True
        >>> list.retrieve(0)
        (5, True)
        >>> list.retrieve(1)
        (6, True)
        >>> list.retrieve(2)
        (8, True)
        >>> list.retrieve(3)
        (None, False)
        """
        if index >= self.getLength() or index < 0:
            return None, False
        current = self.head
        if index == 0:
            return current.getNext().getItem(), True
        else:
            for i in range(0, index + 1):
                current = current.getNext()
            return current.getItem(), True

    def append(self, newItem):
        """
        Testing
        >>> list = LinkedList()
        >>> list.append("A")
        True

        """
        return self.insert(self.getLength(), newItem)

    def getItems(self):
        """
        Testing
        >>> list = LinkedList()
        >>> list.insert(0, "A")
        True
        >>> list.insert(1, "B")
        True
        >>> list.getItems()
        ['A', 'B']
        """
        nodeList = []
        for i in range(0, self.getLength()):
            nodeList.append(self.retrieve(i)[0])
        return nodeList