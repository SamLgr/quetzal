#
# Made by Lander De Roeck on 13/11/17
#

from DoubleNode import doubleNode as Node

class DoubleList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def createList(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = self.head
    
    def destroyList(self):
        if self.isEmpty():
            return False
        self.head = None
        self.tail = None
        return self.isEmpty()

    def getLength(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def __retrieve(self, index):
        if index < 0 or index >= self.getLength():
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def retrieve(self, index):
        node = self.__retrieve(index)
        if node is None:
            return None, False
        return node.getItem(), True

    def __retrieveByValue(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.has_value(value):
                return current_node
            current_node = current_node.next
        return None

    def retrieveByValue(self, value):
        node = self.__retrieveByValue(value)
        if node is None:
            return None, False
        return node.getItem(), True

    def insert(self, index, item):
        length = self.getLength()
        if index < 0 or index > length:
            return False
        elif index == length:
            self.append(item)
            return True
        elif index == 0:
            self.__insertFront(item)
            return True
        new_node = Node(item)
        count = 0
        current_node = self.head
        while count != index:
            count += 1
            current_node = current_node.getNext()
        parent = current_node.prev
        parent.next = new_node
        new_node.prev = parent
        new_node.next = current_node
        current_node.prev = new_node
        return True

    def __insertFront(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head.setPrev(new_node)
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None: # no data present
            self.head = new_node
            self.tail = self.head
        else: # data present
            new_node.setPrev(self.tail)
            self.tail.setNext(new_node)
            self.tail = new_node

    def isEmpty(self):
        return not self.head

    def delete(self, index):
        deleted_node = self.__retrieve(index)
        if deleted_node is None:
            return False
        if deleted_node.prev is None and deleted_node.next is None: # only one node present
            self.head = None
            self.tail = None
        elif deleted_node.prev is None: # node is first, but there are following nodes
            next_node = deleted_node.next
            self.head = next_node
            next_node.prev = None
        elif deleted_node.next is None: # node is last, but there are predecessors
            prev_node = deleted_node.prev
            self.tail = prev_node
            prev_node.next = None
        else: # node is element in middle of list
            next_node = deleted_node.next
            prev_node = deleted_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
        return True

    def deleteByValue(self, value):
        deleted_node = self.__retrieveByValue(value)
        if deleted_node is None:
            return False
        if deleted_node.prev is None and deleted_node.next is None: # only one node present
            self.head = None
            self.tail = None
        elif deleted_node.prev is None: # node is first, but there are following nodes
            next_node = deleted_node.next
            self.head = next_node
            next_node.prev = None
        elif deleted_node.next is None: # node is last, but there are predecessors
            prev_node = deleted_node.prev
            self.tail = prev_node
            prev_node.next = None
        else: # node is element in middle of list
            next_node = deleted_node.next
            prev_node = deleted_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
        return True

    def getItems(self):
        nodeList = []
        nodeList.append(self.head.item)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            nodeList.append(current_node.item)
        return nodeList

    def sort(self):
        if self.isEmpty():
            return False
        itemValues = sorted(self.getItems())
        sortedList = DoubleList()
        for i in itemValues:
            sortedList.append(i)

        self.head = sortedList.head
        self.tail = sortedList.tail

    def first(self):
        """
        >>> list = DoubleList()
        >>> list.append("A")
        >>> list.append("B")
        >>> list.first()
        'A'
        """
        return self.head.item

    def last(self):
        """
        >>> list = DoubleList()
        >>> list.append("A")
        >>> list.append("B")
        >>> list.last()
        'B'
        """
        return self.tail.item

    def traverse(self):
        buffer = []
        current = self.head
        for i in range(self.getLength()):
            buffer.append(current.item)
            current = current.getNext()
        return buffer

    def dotDebug(self):
        graph = self.traverse()
        for i in range(len(graph)):
            graph[i] = str(graph[i])
        print(' -- '.join(graph))

# test = DoubleList()
# test.append(5)
# test.append(6)
# test.dotDebug()
