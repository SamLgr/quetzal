from Stack import Stack
from CircularLinkedList import CircularLinkedList
from BinarySearchTree import BinarySearchTree
from TreeItem import TreeItem
from ourQueue import Queue
from TwoThreeFourTree import TwoThreeFourTree
from DoubleList import DoubleList
from DoubleNode import doubleNode
from Hashmap import Hashmap
from Hashmap import MapObject

def testStack():
    """
                >>> stack = Stack()
                >>> stack.isEmpty()
                True
                >>> stack.push(5)
                True
                >>> stack.isEmpty()
                False
                >>> stack.getTop()
                (5, True)
                >>> stack.push(4)
                True
                >>> stack.getTop()
                (4, True)
                >>> stack.pop()
                (4, True)
                >>> stack.pop()
                (5, True)
                >>> stack.pop()
                (None, False)
    """

def testCirclularLinkedList():
    """
                >>> list = CircularLinkedList()
                >>> list.insert(1, 5)
                False
                >>> list.isEmpty()
                True
                >>> list.insert(0, 5)
                True
                >>> list.isEmpty()
                False
                >>> list.insert(1, 8)
                True
                >>> list.insert(1, 6)
                True
                >>> list.retrieve(1)
                (6, True)
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

def testBST():
    """
                >>> b = BinarySearchTree()
                >>> b.isEmpty()
                True
                >>> b.searchTreeInsert(TreeItem("Test", 5))
                True
                >>> b.isEmpty()
                False
                >>> b.searchTreeInsert(TreeItem("Test Links", 2))
                True
                >>> b.searchTreeInsert(TreeItem("Test Rechts", 9))
                True
                >>> b.searchTreeInsert(TreeItem("Test Rechts Rechts", 11))
                True
                >>> b.searchTreeInsert(TreeItem("Test Rechts Rechts Rechts", 13))
                True
                >>> b.searchTreeInsert(TreeItem("Test Rechts Links", 7))
                True
                >>> b.searchTreeDelete(9)
                True
                >>> b.searchTreeRetrieve(9)
                (None, False)
                >>> b.searchTreeDelete(4)
                False
                >>> b.print() #prints the inorder traversal for testing purposes
                Test Links
                Test
                Test Rechts Links
                Test Rechts Rechts
                Test Rechts Rechts Rechts
    """

def testQueue():
    """
        >>> q = Queue()
        >>> q.isEmpty()
        True
        >>> q.enqueue("A")
        >>> q.enqueue("B")
        >>> q.enqueue("C")
        >>> q.isEmpty()
        False
        >>> q.getLength()
        3
        >>> q.dequeue()
        ('A', True)
        >>> q.traverse()
        ['B', 'C']       
    """

def testTwoThreeFourTree():
    """
        >>> t = TwoThreeFourTree()
        >>> t.isEmpty()
        True
        >>> item = TreeItem("A", 1)
        >>> t.twoThreeFourTreeInsert(item)
        True
        >>> item = TreeItem("B", 2)
        >>> t.twoThreeFourTreeInsert(item)
        True
        >>> item = TreeItem("C", 3)
        >>> t.twoThreeFourTreeInsert(item)
        True
        >>> t.isEmpty()
        False
        >>> t.getTreeLength()
        3
        >>> t.twoThreeFourTreeRetrieve(1)[0].item
        'A'
        >>> t.twoThreeFourTreeRetrieve(3)[0].item
        'C'
        >>> t.twoThreeFourTreeRetrieve(2)[0].item
        'B'
        >>> t.inorderTraverse()
        ['A', 'B', 'C']
        >>> t.inorderTraverse()
        ['A', 'C']
    """

def testDoubleList():
    """
    >>> l = DoubleList()
    >>> l.isEmpty()
    True
    >>> item = doubleNode("Start")
    >>> l.createList(item)
    >>> item = doubleNode("A")
    >>> l.insert(1, item)
    True
    >>> item = doubleNode("B")
    >>> l.insert(2, item)
    True
    >>> item = doubleNode("C")
    >>> l.insert(3, item)
    True
    >>> l.getLength()
    4
    >>> l.retrieve(0)[0].item
    'Start' 
    >>> l.retrieve(1)[0].item
    'A'
    >>> l.retrieveByValue("C")
    True
    >>> item = doubleNode('D')
    >>> l.append(item)
    >>> l.getLength()
    5
    >>> l.first().item
    'Start'
    >>> l.last().item
    'D'
    >>> l.append(5)
    >>> l.retrieveByValue(5)
    (5, True)
    """

def testHashmap():
    """
    >>> hmap = Hashmap(1, 50)
    >>> hmap.isEmpty()
    True
    >>> hmap.getLength()
    0
    >>> item = MapObject(1, "A")
    >>> hmap.insert(item)
    True
    >>> item = MapObject(2, "B")
    >>> hmap.insert(item)
    True
    >>> item = MapObject(2, "C")
    >>> hmap.insert(item)
    True
    >>> item = MapObject(3, "D")
    >>> hmap.insert(item)
    True
    >>> hmap.getLength()
    4
    >>> hmap.isEmpty()
    False
    >>> hmap.retrieve(2)
    'B'
    >>> hmap.retrieve(3)
    'D'
    """
