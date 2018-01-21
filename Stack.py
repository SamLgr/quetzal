from Node import Node

class Stack:
    def __init__(self):
        """
        Initialiseert een lege stack

        >>> Stack().top is None
        True
        """
        self.top = None

    def __del__(self):
        self.top = None

    def isEmpty(self):
        """
        Bepaalt of de stack leeg is.
        :return: bool die aangeeft of de stack leeg is

        >>> stack = Stack()
        >>> stack.isEmpty()
        True
        >>> stack.push(5)
        True
        >>> stack.isEmpty()
        False
        """
        return self.top is None

    def push(self, newItem):
        """
        Voegt element 'newItem' toe op top van de stack.
        :param newItem: element dat moet worden toegevoegd
        :return: bool die aangeeft of het toevoegen gelukt is

        >>> stack = Stack()
        >>> stack.push(5)
        True
        >>> stack.getTop()
        (5, True)
        >>> stack.push(4)
        True
        >>> stack.getTop()
        (4, True)
        """
        node = Node(newItem, self.top)
        self.top = node
        return True

    def pop(self):
        """
        Verwijdert element op de top van de stack.
        :return: top van stack die verwijderd werd, bool die aangeeft of het verwijderen gelukt is

        >>> stack = Stack()
        >>> stack.push(5)
        True
        >>> stack.pop()
        (5, True)
        >>> stack.isEmpty()
        True
        """
        if self.isEmpty():
            return None, False
        stackTop = self.top.getItem()
        self.top = self.top.getNext()
        return stackTop, True

    def getTop(self):
        """
        Geeft top van stack terug
        :return: top van stack, bool die aangeeft of het ophalen gelukt is

        >>> stack = Stack()
        >>> stack.getTop()
        (None, False)
        >>> stack.push(5)
        True
        >>> stack.getTop()
        (5, True)
        """
        if self.isEmpty():
            return None, False
        return self.top.getItem(), True

    def getItems(self):
        buffer = []
        current = self.top
        while current is not None:
            buffer.append(current.getItem())
            current = current.getNext()
        return buffer[::-1]