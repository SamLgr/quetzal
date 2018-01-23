#
# Made by Lander De Roeck on 13/11/17
#

from DoubleNode import doubleNode as Node

class DoubleList(object):
    #Constructor
    def __init__(self):
        self.head = None
        self.tail = None
    
    #Creates a new DoubleList
    #:param data: Initial data to add
    def createList(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = self.head
    
    #Destroys the list
    #:return bool: Return True if succesful
    def destroyList(self):
        if self.isEmpty():
            return False
        self.head = None
        self.tail = None
        return self.isEmpty()

    #Returns the length of the list
    def getLength(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    #Internal function,
    #Retrieves the node at 'index'
    #:param index: int -> Index to get node at
    #:return Node: node at 'index'
    def __retrieve(self, index):
        if index < 0 or index >= self.getLength():
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    #Returns the value at 'index'
    #:param index: Int -> index to get value at
    #:return ListItem: Item at 'index'
    def retrieve(self, index):
        node = self.__retrieve(index)
        if node is None:
            return None, False
        return node.getItem(), True

    #Searches the list by 'value' at returns
    #node with that value
    #:param value: Value to search for
    #:return Node: node with 'value'
    def __retrieveByValue(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.has_value(value):
                return current_node
            current_node = current_node.next
        return None

    #Searches list for 'value' and returns that value if found
    #:param value: Value to search list for
    #:return ListItem: Value to be returned if found
    def retrieveByValue(self, value):
        node = self.__retrieveByValue(value)
        if node is None:
            return None, False
        return node.getItem(), True

    #Inserts a value into the list
    #:param index: Int -> Index to insert at
    #:param item: Value to insert
    #:return bool: Returns True if succesful
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

    #Inserts 'data' in front of list
    #:param data: Data to set in front
    def __insertFront(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head.setPrev(new_node)
        self.head = new_node

    #Adds 'data' to the end of the list
    #:param data: Data to add to the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None: # no data present
            self.head = new_node
            self.tail = self.head
        else: # data present
            new_node.setPrev(self.tail)
            self.tail.setNext(new_node)
            self.tail = new_node

    #Returns True if list is empty
    def isEmpty(self):
        return not self.head

    #Deletes item at 'index' in Tree
    #:param index: index to delete item at
    #:return bool: Returns True if succesful
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

    #Searches the list for 'value' and deletes that node when found
    #:param value: Value to delete
    #:param bool: Returns True if succesful
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

    #Returns all the items in a list
    def getItems(self):
        nodeList = []
        nodeList.append(self.head.item)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            nodeList.append(current_node.item)
        return nodeList

    #Sorts all the items in the list
    def sort(self):
        if self.isEmpty():
            return False
        itemValues = sorted(self.getItems())
        sortedList = DoubleList()
        for i in itemValues:
            sortedList.append(i)

        self.head = sortedList.head
        self.tail = sortedList.tail

    #Returns first element in the list
    def first(self):
        """
        >>> list = DoubleList()
        >>> list.append("A")
        >>> list.append("B")
        >>> list.first()
        'A'
        """
        return self.head.item

    #Returns last element in the list
    def last(self):
        """
        >>> list = DoubleList()
        >>> list.append("A")
        >>> list.append("B")
        >>> list.last()
        'B'
        """
        return self.tail.item

    #Returns all element in the list as a list
    def traverse(self):
        buffer = []
        current = self.head
        for i in range(self.getLength()):
            buffer.append(current.item)
            current = current.getNext()
        return buffer

    #Used to create a graphical representation of the list
    def dotDebug(self):
        debugstring = []
        graph = self.traverse()
        if len(graph) == 0:
            return debugstring
        if len(graph) == 1:
            debugstring.append(str(graph[0]))
            return debugstring
        for i in range(1, len(graph)):
            debugstring.append("\"" + str(graph[i - 1]) + '\" -- \"' + str(graph[i]) + "\"")
        return debugstring

    def writeDotFile(self):
        debugstring = ["digraph G {"]
        debugstring.extend(self.dotDebug())
        debugstring.append("}")
        file = open('dll.dot', 'w+')
        file.write("\n".join(debugstring))

# test = DoubleList()
# test.append('5a')
# test.append('6a')
# print(test.retrieveByValue('5a'))
# test.append(50)
# test.append("qkqke")
# test.writeDotFile()
