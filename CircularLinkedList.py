from Node import Node

class CircularLinkedList:
    def __init__(self):
        """
        Initialises an empty circular linked list.

        >>> head = CircularLinkedList().head
        >>> head.item == None
        True
        >>> head.getNext() == head
        True
        """
        self.head = Node(None, None)
        self.head.setNext(self.head)

    def __del__(self):
        """
        Reinitialises circular linked list to an empty one.
        """
        self.head = Node(None, None)
        self.head.setNext(self.head)

    def isEmpty(self):
        """
        Determines whether circular linked list is empty or not
        :return: bool indicating if circular linked list is empty

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
        Determines length of circular linked list.
        :return: length of circular linked list

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
        Inserts element 'newItem' at position 'index' in circular linked list.
        :param index: position where 'newItem' has to be inserted
        :param newItem: element to be inserted
        :return: bool indicating if insert was successful

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
        :param index: position of element to be deleted
        :return: bool indicating if delete was successful

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
        Returns element at position 'index' in circular linked list.
        :param index: position of element to be retrieved
        :return: element at position 'index', bool indicating if retrieve was successful

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
    
    def append(self, newItem):
        """
        Appends element to circular linked list.
        :param newItem: element to append
        :return: bool indicating if append was successful

        >>> list = CircularLinkedList()
        >>> list.append("A")
        True
       
        """
        return self.insert(self.getLength(), newItem)
 
    def getItems(self):
        """
        Returns all elements in circular linked list in sequential order.
        :return: list containing elements in circular linked list

        >>> list = CircularLinkedList()
        >>> list.append("A")
        True
        >>> list.append("B")
        True
        >>> list.getItems()
        ['A', 'B']
        """
        nodeList = []
        for i in range(0, self.getLength()):
            nodeList.append(self.retrieve(i)[0])
        return nodeList

    def first(self):
        """
        Returns first element in circular linked list.
        :return: first element in circular linked list

        >>> l = CircularLinkedList()
        >>> l.append("A")
        True
        >>> l.append("B")
        True
        >>> l.append("C")
        True
        >>> l.first()
        'A'
        """
        return self.getItems()[0]

    def last(self):
        """
        Returns last element in circular linked list.
        :return: last element in circular linked list

        >>> l = CircularLinkedList()
        >>> l.append("A")
        True
        >>> l.append("B")
        True
        >>> l.append("C")
        True
        >>> l.last()
        'C'
        """
        return self.getItems()[len(self.getItems()) - 1]
