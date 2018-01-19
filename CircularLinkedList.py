from Node import Node

class CircularLinkedList:
    def __init__(self):
        """
        Initialiseert een lege circulair gelinkte lijst

        >>> head = CircularLinkedList().head
        >>> head.item == None
        True
        >>> head.getNext() == head
        True
        """
        self.head = Node(None, None)
        self.head.setNext(self.head)

    def __del__(self):
        self.head = Node(None, None)
        self.head.setNext(self.head)

    def isEmpty(self):
        """
        Bepaalt of de circulair gelinkte lijst leeg is
        :return: bool die aangeeft of de lijst leeg is

        >>> list = CircularLinkedList()
        >>> list.isEmpty()
        True
        >>> list.insert(0, 5)
        True
        >>> list.isEmpty()
        False
        """
        return self.head.getNext() == self.head

    def getLength(self):
        """
        Bepaalt de lengte van de circulair gelinkte lijst
        :return: lengte van de circulair gelinkte lijst

        >>> list = CircularLinkedList()
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
        while current is not self.head:
            current = current.getNext()
            count+=1
        return count

    def insert(self, index, newItem):
        """
        Voegt element 'newItem' toe op positie 'index' in de circulair gelinkte lijst.
        :param index: positie waar 'newItem' moet worden toegevoegd
        :param newItem: element dat moet worden toegevoegd
        :return: bool die aangeeft of het toevoegen gelukt is

        >>> list = CircularLinkedList()
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
        if index == self.getLength():
            node = Node(newItem, current.getNext())
            current.setNext(node)
            self.head = node
        else:
            for i in range(0, index+2):
                previous = current
                current = current.getNext()
            node = Node(newItem, current)
            previous.setNext(node)
        return True

    def delete(self, index):
        """
        Verwijdert element op positie 'index' uit de circulair gelinkte lijst.
        :param index: positie van element dat moet worden verwijderd
        :return: bool die aangeeft of het verwijderen gelukt is

        >>> list = CircularLinkedList()
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
        length = self.getLength()
        for i in range(0, index+2):
            previous = current
            current = current.getNext()
        previous.setNext(current.getNext())
        if index == length-1:
            self.head = previous
        return True

    def retrieve(self, index):
        """
        Geeft element op positie 'index' in de circulair gelinkte lijst terug.
        :param index: positie van het element
        :return: element op positie 'index', bool die aangeeft of het ophalen gelukt is

        >>> list = CircularLinkedList()
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
        if index == self.getLength()-1:
            return current.item, True
        else:
            for i in range(0, index+2):
                current = current.getNext()
            return current.item, True
    
    def append(self, data):
        """
        Testing
        >>> list = CircularLinkedList()
        >>> list.append("A")
        True
       
        """
        new_node = Node(data)
        if self.head is None: # no data present
            self.head = new_node
            self.head.setNext(new_node)
        else: # data present
            new_node.setNext(self.head.next)
            self.head.setNext(new_node)
            self.head.next = new_node

        return True
 
    def getItems(self):
        """
        Testing
        >>> list = CircularLinkedList()
        >>> list.append("A")
        True
        >>> list.append("B")
        True
        >>> list.getItems()
        ['A', 'B']
        """
        nodeList = []
        current_node = self.head.getNext()
        while current_node is not self.head:
            nodeList.append(current_node.item)
            current_node = current_node.next
           
        return nodeList[::-1]
