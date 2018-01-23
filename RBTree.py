#
# Made by Lander De Roeck on 26/11/17
# Inspiration: https://www.cs.auckland.ac.nz/software/AlgAnim/red_black.html
#
from DoubleList import DoubleList

class TreeItem(object):
    # added to support different values, not only ints
    #:param value: initial value to set
    #:param key: key to identify item
    def __init__(self, value, key):
        self.value = DoubleList()
        self.insert(value)
        self.key = key

    #Insert value in Tree
    def insert(self, value):
        self.value.append(value)

    #Returns element in Tree
    def retrieve(self):
        return self.value.traverse()

class rbNode(object):
    #Constructor
    #:param item: Item for this Node
    #:param colour: Colour for this Node (red/black)
    #:param parent: Pointer to parent of this Node
    #:param leftTree: Pointer to Node left of this Tree
    #:param rightTree: Pointer to Node right of this Tree
    def __init__(self, item=None, colour=False, parent=None, leftTree=None, rightTree=None):
        self.item = item
        self.red = colour
        self.parent = parent
        self.leftTree = leftTree
        self.rightTree = rightTree
    
    #Returns the key of this Node
    def getKey(self):
        return self.item.key

    
    def isLeaf(self):  # checks if node is leaf
        return not self.leftTree and not self.rightTree

    def dotDebug(self):  # debug code to represent tree in dot language
        debugstring = []
        if not self.parent and self.isLeaf():  # tree only has one item (root)
            debugstring.append(self.item.retrieve()[0])
            return debugstring
        if self.parent and self.item:
            strprint = "\"" + ", ".join(self.parent.item.retrieve()) + "\" -> \"" + ", ".join(self.item.retrieve()) + "\""
            if self.red:
                strprint = strprint + " [style=dashed];"
            else:
                strprint = strprint + ";"
            debugstring.append(strprint)
        if self.leftTree:
            debugstring.extend(self.leftTree.dotDebug())
        if self.rightTree:
            debugstring.extend(self.rightTree.dotDebug())
        return debugstring

    def writeDotFile(self):
        debugstring = ["digraph G {"]
        debugstring.extend(self.dotDebug())
        debugstring.append("}")
        file = open('rbt.dot', 'w+')
        file.write("\n".join(debugstring))

    def retrieveItemNode(self, key):  # returns node with key value
        if key == self.getKey():
            return self
        elif key < self.getKey():
            if self.leftTree is None:
                return None
            x = self.leftTree.retrieveItemNode(key)
            return x
        elif key > self.getKey():
            if self.rightTree is None:
                return None
            x = self.rightTree.retrieveItemNode(key)
            return x
    
    def retrieveItem(self, key):  # returns values with key
        if key == self.getKey():
            return self.item.retrieve(), True
        elif key < self.getKey():
            if self.leftTree is None:
                return None, False
            x = self.leftTree.retrieveItem(key)
            return x
        elif key > self.getKey():
            if self.rightTree is None:
                return None, False
            x = self.rightTree.retrieveItem(key)
            return x

    def treeSuccessor(self):  # finds successor and returns that node
        if self.rightTree is not None:
            node = self.rightTree
            while node.leftTree is not None:
                node = node.leftTree
            return node
        else:
            return self.leftTree

    #Returns a list of all the elements in Tree in order
    def inorderTraverse(self):
        traverseList = []
        if self.leftTree is not None:
            traverseList.extend(self.leftTree.inorderTraverse())
        traverseList.extend(self.item.retrieve())
        if self.rightTree is not None:
            traverseList.extend(self.rightTree.inorderTraverse())
        return traverseList


class redBlackTree(object):
    #Constructor
    #:param root: Set initial node of the Tree
    def __init__(self, root=None):
        self.root = root
    
    def createRBTree(self, item):  # creates initial node
        root = rbNode(item)
        self.root = root

    def destroyRBTree(self):  # __del__
        # delete values
        self.root = None
    
    #Returns True if tree is empty
    def isEmtpy(self):
        return self.root is None

    #Inserts 'item' in the Tree
    #:param item: Item to add
    #:return bool: Returns True if succesful
    def insertItem(self, item):
        if self.isEmtpy():  # if tree is empty, insert root
            self.createRBTree(item)
            return True
        # create leaf node with value as root
        node = rbNode(item, True)
        # create check value
        check_node = self.root
        while check_node:
            node.parent = check_node
            if check_node.getKey() > node.getKey():
                check_node = check_node.leftTree
            elif check_node.getKey() < node.getKey():
                check_node = check_node.rightTree
            else:
                check_node.item.insert(node.item.retrieve()[0])
                return True
        if node.getKey() < node.parent.getKey():
            node.parent.leftTree = node
        else:
            node.parent.rightTree = node
        self.insert_fix(node)
        return True

    #Makes sure the RBTree remains a RBTree after insert
    def insert_fix(self, x):
        while x.parent.red:
            if x.parent == x.parent.parent.leftTree:  # parent is left tree (parent is red, so can't be root, therefore has a parent)
                y = x.parent.parent.rightTree 
                if y and y.red:  # both node, parent and parent's sibling are red
                    x.parent.red = False 
                    y.red = False
                    x.parent.parent.red = True
                    x = x.parent.parent
                else:  # parent's sibling isn't red
                    if x == x.parent.rightTree:
                        x = x.parent
                        self.leftRotate(x)
                    else:
                        x.parent.red = False
                        x.parent.parent.red = True
                        self.rightRotate(x.parent.parent)
            else:  # parent is right tree
                y = x.parent.parent.leftTree
                if y and y.red:
                    x.parent.red = False
                    y.red = False
                    x.parent.parent.red = True
                    x = x.parent.parent
                else:
                    if x == x.parent.leftTree:
                        x = x.parent
                        self.rightRotate(x)
                    else:
                        x.parent.red = False
                        x.parent.parent.red = True
                        self.leftRotate(x.parent.parent)
            if x == self.root:
                break
        self.root.red = False

    #Launches the rotate-left algorithm on the Tree
    def leftRotate(self, x):
        y = x.rightTree

        x.rightTree = y.leftTree
        if y.leftTree:
            y.leftTree.parent = x
        
        y.parent = x.parent
        if not x.parent:  # node is root
            self.root = y
        
        elif x == x.parent.leftTree:
            x.parent.leftTree = y
        else:
            x.parent.rightTree = y

        y.leftTree = x
        x.parent = y

    #Launches the rotate-right algorithm on the Tree
    def rightRotate(self, y):
        x = y.leftTree

        y.leftTree = x.rightTree
        if x.rightTree:
            x.rightTree.parent = y

        x.parent = y.parent
        if not y.parent:
            self.root = x

        elif y == y.parent.rightTree:
            y.parent.rightTree = x
        else:
            y.parent.leftTree = x

        x.rightTree = y
        y.parent = x
    
    #Gives graphical representation of the Tree
    def dotDebug(self):  # function that calls on debug code
        if self.isEmtpy():
            return False
        self.root.writeDotFile()

    #Deletes an item from the tree
    #:param key: Key of Node to delete
    #:return bool: Returns True if succesful
    def deleteItem(self, key):
        # retrieving node
        z = self.root.retrieveItemNode(key)
        # check if node is valid
        if z is None:
            return False
        
        if z.leftTree is None or z.rightTree is None:
            y = z
        else:  # node has two children
            y = z.treeSuccessor()

        if y.leftTree is not None:
            x = y.leftTree
        else:
            x = y.rightTree
        
        # check if x node is not none
        if x is not None:
            x.parent = y.parent

        if y.parent is None:  # y is root
            self.root = x
        elif y == y.parent.leftTree:  # y is left child
            y.parent.leftTree = x
        else:  # y is right child
            y.parent.rightTree = x

        if y != z:  # make sure the value in the node is overridden
            z.item = y.item

        if not y.red and x is not None:  # call on fix is y was red, and x (y's sibling) is not none
            self.delete_fix(x)

        return True

    #Makes sure the RBTree remains a RBTree after deleting a Node
    def delete_fix(self, x):
        while x != self.root and not x.red:
            if x == x.parent.leftTree:
                w = x.parent.rightTree
                if w.red:
                    w.red = False
                    x.parent.red = True
                    self.leftRotate(x.parent)
                    w = x.parent.rightTree
                if not w.leftTree.red and not w.rightTree.red:
                    w.red = True
                    x = x.parent
                elif not w.rightTree.red:
                    w.leftTree.red = False
                    w.red = True
                    self.rightRotate(w)
                    w = x.parent.rightTree
                else:
                    w.red = x.parent.red
                    x.parent.red = False
                    w.rightTree.red = False
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.leftTree
                if w.red:
                    w.red = False
                    x.parent.red = True
                    self.rightRotate(x.parent)
                    w = x.parent.leftTree
                if not w.rightTree.red and not w.leftTree.red:
                    w.red = True
                    x = x.parent
                elif not w.leftTree.red:
                    w.rightTree.red = False
                    w.red = True
                    self.leftRotate(w)
                    w = x.parent.leftTree
                else:
                    w.red = x.parent.red
                    x.parent.red = False
                    w.leftTree.red = False
                    self.rightRotate(x.parent)
                    x = self.root
        x.red = False

    #Returns all the elements of the tree in a list, in order
    def inorderTraverse(self):
        return self.root.inorderTraverse()

    #Returns the amount of nodes in the tree
    def getLength(self):
        list = self.root.inorderTraverse
        return len(list)

    #Returns the Item with 'key'
    #:param key: Key to retrieve item with
    #:return TreeItem: Item mapped to 'key' and to be returned
    def retrieveItem(self, key):
        return self.root.retrieveItem(key)



# test = redBlackTree()
# test.insertItem(TreeItem("a", 1))
# test.insertItem(TreeItem("b", 5))
# test.insertItem(TreeItem("ff", 5))
# test.insertItem(TreeItem("c", 50))
# test.insertItem(TreeItem("d", 10))
# test.insertItem(TreeItem("woop", 15))
# test.deleteItem(50)
# test.deleteItem(15)
# test.dotDebug()
