#
# Made by Lander De Roeck on 26/11/17
# Inspiration: https://www.cs.auckland.ac.nz/software/AlgAnim/red_black.html
#


class rbNode(object):
    def __init__(self, value=None, colour=False, parent=None, leftTree=None, rightTree=None):
        self.value = value
        self.red = colour
        self.parent = parent
        self.leftTree = leftTree
        self.rightTree = rightTree
    
    def isLeaf(self):
        return not self.leftTree and not self.rightTree

    def dotDebug(self):
        if self.parent and self.value:
            strprint = str(self.parent.value) + " -> " + str(self.value)
            if self.red:
                strprint = strprint + " [style=dashed];"
            else:
                strprint = strprint + ";"
            print(strprint)
        if self.leftTree:
            self.leftTree.dotDebug()
        if self.rightTree:
            self.rightTree.dotDebug()
    
    def retrieveItem(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            if self.leftTree is None:
                return None
            x = self.leftTree.retrieveItem(value)
            return x
        elif value > self.value:
            if self.rightTree is None:
                return None
            x = self.rightTree.retrieveItem(value)
            return x

    def treeSuccessor(self):
        if self.rightTree is not None:
            node = self.rightTree
            while node.leftTree is not None:
                node = node.leftTree
            return node
        else:
            return self.leftTree


class redBlackTree(object):
    def __init__(self, root=None):
        self.root = root
    
    def createRBTree(self, value):
        root = rbNode(value)
        self.root = root

    # def getLeftTree(self):
    #     return self.leftTree

    # def getRightTree(self):
    #     return self.rightTree

    # def getRoot(self):
    #     return self.root

    def destroyRBTree(self):  # __del__
        # delete values
        self.root = None
    
    def isEmtpy(self):
        return self.root is None

    def insertItem(self, value):
        if self.isEmtpy():  # if tree is empty, insert root
            self.createRBTree(value)
            return True
        # create leaf node with value as root
        node = rbNode(value, True)
        # create check value
        check_node = self.root
        while check_node:
            node.parent = check_node
            if check_node.value > node.value:
                check_node = check_node.leftTree
            elif check_node.value < node.value:
                check_node = check_node.rightTree
            else:
                return False  # TODO change to account for multiple things with same keyvalue
        if node.value < node.parent.value:
            node.parent.leftTree = node
        else:
            node.parent.rightTree = node
        self.insert_fix(node)

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
    
    # def traverse(self):
    #     if self.leftTree is not None:
    #         self.leftTree.inorderTraverse()
    #     print(self.root)
    #     if self.rightTree is not None:
    #         self.rightTree.inorderTraverse()

    # def deleteItem(self, value):
    #     delete_Node = self.root.retrieveItem(value)
    #     if delete_Node is None:
    #         return False
    #     if delete_Node.leftTree is None and delete_Node.rightTree is None:
    #         delete_Node = None
    #     elif delete_Node.leftTree is not None and delete_Node.rightTree is None:
    #         parent = delete_Node.parent
    #         delete_Node = delete_Node.leftTree
    #         delete_Node.parent = parent
    #     elif delete_Node.rightTree is not None and delete_Node.leftTree is None:
    #         parent = delete_Node.parent
    #         delete_Node = delete_Node.rightTree
    #         delete_Node.parent = parent
    #     else:
    #         parent_Node = delete_Node
    #         currentTree = delete_Node.rightTree
    #         while currentTree.leftTree is not None:
    #             currentTree = currentTree.leftTree
    #         parent = currentTree.parent
    #         delete_Node.value = currentTree.value
    #         currentTree = currentTree.rightTree
    #         currentTree.parent = parent
    #     # self.delete_fix() #doesn't work yet
    #     return  True

        
    # def getLength(self):
    #     pass
    
    def dotDebug(self):
        self.root.dotDebug()

    def deleteItem(self, value):
        z = self.root.retrieveItem(value)
        if z is None:
            return False

        if z.leftTree is None or z.rightTree is None:
            y = z
        else:
            y = z.treeSuccessor()

        if y.leftTree is not None:
            x = y.leftTree
        else:
            x = y.rightTree

        if x is not None:
            x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.leftTree:
            y.parent.leftTree = x
        else:
            y.parent.rightTree = x

        if y != z:
            z.value = y.value

        if not y.red and x is not None:
            self.delete_fix(x)

        return y

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
