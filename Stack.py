from Node import Node

class Stack:
    def __init__(self):
        """
        Initialises an empty stack:

        >>> Stack().top is None
        True
        """
        self.top = None

    def __del__(self):
        self.top = None

    def isEmpty(self):
        """
        Determines whether the stack is empty or not.
        :return: bool indicating if stack is empty

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
        Pushes element 'newItem' on top of the stack.
        :param newItem: element to be pushed
        :return: bool indicating if push was successful

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
        Pops element from top of the stack.
        :return: Popped element, bool indicating if pop was successful

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
        Returns top of the stack.
        :return: top of the stack, bool indicating if getTop was successful

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

    def traverse(self):
        """
        Returns list of all elements in the stack from bottom to top.
        :return: list of all elements in the stack

        >>> stack = Stack()
        >>> stack.push(5)
        True
        >>> stack.getTop()
        (5, True)
        >>> stack.push(4)
        True
        >>> stack.getTop()
        (4, True)
        >>> stack.traverse()
        [5, 4]
        """
        traverselist = []
        current = self.top
        while current is not None:
            traverselist.append(current.getItem())
            current = current.getNext()
        return traverselist[::-1]