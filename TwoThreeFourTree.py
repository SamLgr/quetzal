from TreeItem import TreeItem
from CircularLinkedList import CircularLinkedList

class TwoThreeFourTree:
    def __init__(self):
        self.root = CircularLinkedList()
        self.parent = None
        self.left = None
        self.leftmid = None #Will be used as mid in case of a 3-node
        self.rightmid = None
        self.right = None

    def __del__(self):
        self.root = CircularLinkedList()
        self.parent = None
        self.left = None
        self.leftmid = None
        self.rightmid = None
        self.right = None

    def isEmpty(self):
        """
        Tests if TwoThreeFourTree is empty
        :return: True if empty, False if not empty
        """
        return self.root.isEmpty()

    def twoThreeFourTreeInsert(self, TreeItem):
        """
        Inserts given TreeItem at right place in TwoThreeFourTree
        :param TreeItem: TreeItem to be inserted
        :return: True if succeeded, False if not succeeded
        >>> t = TwoThreeFourTree()
        >>> t.twoThreeFourTreeInsert(TreeItem("Test", 5))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 2", 7))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 2", 9))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 2", 11))
        True
        >>> t.right.root.retrieve(1)[0].getKey()
        11
        """
        isLeaf = self.left is None and self.leftmid is None and self.rightmid is None and self.right is None
        if self.root.getLength() < 3:  # Node is 2-node or 3-node
            if isLeaf:  #Node is a leaf
                return self.__nodeInsert(TreeItem)
            else:   #Node is not a leaf
                if self.root.getLength() == 1:  #Node is 2-node, find child Tree to insert TreeItem
                    if self.root.retrieve(0)[0].getKey() < TreeItem.getKey():
                            return self.right.twoThreeFourTreeInsert(TreeItem)
                    elif self.root.retrieve(0)[0].getKey() > TreeItem.getKey():
                            return self.left.twoThreeFourTreeInsert(TreeItem)
                    else:
                        return False
                elif self.root.getLength() == 2:    #Node is 3-node, find child Tree to insert TreeItem
                    if self.root.retrieve(0)[0].getKey() < TreeItem.getKey():
                        if self.root.retrieve(1)[0].getKey() < TreeItem.getKey():
                            return self.right.twoThreeFourTreeInsert(TreeItem)
                        else:
                            return self.leftmid.twoThreeFourTreeInsert(TreeItem)
                    else:
                        return self.left.twoThreeFourTreeInsert(TreeItem)
        else:  # Node is 4-node
            self.__split()
            if self.parent is None:     #Insert for root
                return self.twoThreeFourTreeInsert(TreeItem)
            else:       #Insert for internal node, insert in parent (if parent is a 4-node use custom algorithm because parent does not have to be split)
                if self.parent.root.getLength() < 3:
                    return self.parent.twoThreeFourTreeInsert(TreeItem)
                else:
                    if self.parent.root.retrieve(0)[0].getKey() < TreeItem.getKey():
                        if self.parent.root.retrieve(1)[0].getKey() < TreeItem.getKey():
                            return self.parent.right.twoThreeFourTreeInsert(TreeItem)
                        else:
                            return self.parent.leftmid.twoThreeFourTreeInsert(TreeItem)
                    else:
                        return self.parent.left.twoThreeFourTreeInsert(TreeItem)


    def __nodeInsert(self, TreeItem):
        for i in range(self.root.getLength()):  # Insert at right place in Node
            if self.root.retrieve(i)[0] is not None:
                if self.root.retrieve(i)[0].getKey() > TreeItem.getKey():
                    self.root.insert(i, TreeItem)
                    return True
        self.root.insert(self.root.getLength(), TreeItem)
        return True

    def __split(self):
        if self.parent is None: #Node is root of tree
            if self.left is None: #Create left Tree if it does not exist
                self.left = TwoThreeFourTree()
            else:
                pointer = self.left #Reconnect left children (left becomes left.left, leftmid becomes left.right)
                self.left = TwoThreeFourTree()
                self.left.left = pointer
                self.left.left.parent = self.left
            self.left.parent = self
            if self.leftmid is not None:
                self.left.right = self.leftmid
                self.left.right.parent = self.left
            if self.right is None: #Create right Tree if it does not exist
                self.right = TwoThreeFourTree()
            else:
                pointer = self.right #Reconnect right children (rightmid becomes right.left, right becomes right.right)
                self.right = TwoThreeFourTree()
                self.right.right = pointer
                self.right.right.parent = self.right
            self.right.parent = self
            if self.rightmid is not None:
                self.right.left = self.rightmid
                self.right.left.parent = self.right #Set the appropriate parents
            self.left.root.insert(0, self.root.retrieve(0)[0])  #Move first and last element to left and right Trees
            self.right.root.insert(0, self.root.retrieve(2)[0])
            self.root.delete(2)
            self.root.delete(0)
            self.leftmid = None
            self.rightmid = None

        else:   #Node is internal
            self.parent.__nodeInsert(self.root.retrieve(1)[0])
            if self.parent.root.getLength() == 2:   #Parent Node is 2-node
                if self.parent.left == self:    #Tree is leftTree of Parent
                    self.parent.leftmid = TwoThreeFourTree()
                    self.parent.leftmid.root.insert(0, self.root.retrieve(2)[0])
                    self.parent.leftmid.parent = self.parent    #Reconnect 2 subtrees to new subtree
                    self.parent.leftmid.left = self.rightmid
                    self.parent.leftmid.right = self.right
                    if self.rightmid is not None:   #Set the appropriate parents
                        self.parent.leftmid.left.parent = self.leftmid
                    if self.right is not None:
                        self.parent.leftmid.right.parent = self.leftmid
                    self.right = self.leftmid   #Shift subtrees and delete duplicates
                    self.leftmid = None
                    self.rightmid = None
                    self.root.delete(2)
                    self.root.delete(1)
                elif self.parent.right == self: #Tree is rightTree of Parent, same algorithm as above but tweaked for other subtree
                    self.parent.leftmid = TwoThreeFourTree()
                    self.parent.leftmid.root.insert(0, self.root.retrieve(0)[0])
                    self.parent.leftmid.parent = self.parent
                    self.parent.leftmid.left = self.left
                    self.parent.leftmid.right = self.leftmid
                    if self.left is not None:
                        self.parent.leftmid.left.parent = self.leftmid
                    if self.leftmid is not None:
                        self.parent.leftmid.right.parent = self.leftmid
                    self.left = self.rightmid
                    self.leftmid = None
                    self.rightmid = None
                    self.root.delete(1)
                    self.root.delete(0)
            elif self.parent.root.getLength() == 3: #Parent Node is 3-node
                if self.parent.left == self: #Tree is leftTree of Parent, idem
                    self.parent.rightmid = self.parent.leftmid
                    self.parent.leftmid = TwoThreeFourTree()
                    self.parent.leftmid.root.insert(0, self.root.retrieve(2)[0])
                    self.parent.leftmid.parent = self.parent
                    self.parent.leftmid.left = self.rightmid
                    self.parent.leftmid.right = self.right
                    if self.rightmid is not None:
                        self.parent.leftmid.left.parent = self.leftmid
                    if self.right is not None:
                        self.parent.leftmid.right.parent = self.leftmid
                    self.right = self.leftmid
                    self.leftmid = None
                    self.rightmid = None
                    self.root.delete(2)
                    self.root.delete(1)
                elif self.parent.leftmid == self: #Tree is midTree of Parent, idem
                    self.parent.rightmid = TwoThreeFourTree()
                    self.parent.rightmid.root.insert(0, self.root.retrieve(2)[0])
                    self.parent.rightmid.parent = self.parent
                    self.parent.rightmid.left = self.rightmid
                    self.parent.rightmid.right = self.right
                    if self.rightmid is not None:
                        self.parent.rightmid.left.parent = self.rightmid
                    if self.right is not None:
                        self.parent.rightmid.right.parent = self.rightmid
                    self.right = self.leftmid
                    self.leftmid = None
                    self.rightmid = None
                    self.root.delete(2)
                    self.root.delete(1)
                elif self.parent.right == self: #Tree is rightTree of Parent, idem
                    self.parent.rightmid = TwoThreeFourTree()
                    self.parent.rightmid.root.insert(0, self.root.retrieve(0)[0])
                    self.parent.rightmid.parent = self.parent
                    self.parent.rightmid.left = self.left
                    self.parent.rightmid.right = self.leftmid
                    if self.left is not None:
                        self.parent.rightmid.left.parent = self.rightmid
                    if self.leftmid is not None:
                        self.parent.rightmid.right.parent = self.rightmid
                    self.left = self.rightmid
                    self.leftmid = None
                    self.rightmid = None
                    self.root.delete(1)
                    self.root.delete(0)

    def twoThreeFourTreeDelete(self, key):
        """
        Deletes TreeItem with given key out of TwoThreeFourTree
        :param key: key of TreeItem to be deleted
        :return: True if succeeded, False if not succeeded
        >>> t = TwoThreeFourTree()
        >>> t.twoThreeFourTreeInsert(TreeItem("Test", 5))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 2", 7))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 2", 9))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 2", 11))
        True
        >>> t.right.root.retrieve(1)[0].getKey()
        11
        >>> t.twoThreeFourTreeDelete(7)
        True
        >>> t.twoThreeFourTreeRetrieve(7)
        False
        """
        if self.root.getLength() > 1 or self.parent is None:   #Node is 3-node or 4-node
            isLeaf = self.left is None and self.leftmid is None and self.rightmid is None and self.right is None
            for i in range(self.root.getLength()): #Check if key is in node
                if self.root.retrieve(i)[0].getKey() == key:
                    if isLeaf:
                        self.root.delete(i)
                    else:   #Swap with inorder successor if key is not in node
                        self.root.insert(i, self.__getInorderSuccesor(i))
                        self.root.delete(i+1)
                    return True
            if self.root.getLength() == 1: #Node is root, delete in appropriate subtree
                if self.root.retrieve(0)[0].getKey() < key:
                    if self.right is not None:
                        return self.right.twoThreeFourTreeDelete(key)
                else:
                    if self.left is not None:
                        return self.left.twoThreeFourTreeDelete(key)
            elif self.root.getLength() == 2:  #Node is 3-node, delete in appropriate subtree
                if self.root.retrieve(0)[0].getKey() < key:
                    if self.root.retrieve(1)[0].getKey() < key:
                        if self.right is not None:
                            return self.right.twoThreeFourTreeDelete(key)
                        else:
                            return False
                    else:
                        if self.leftmid is not None:
                            return self.leftmid.twoThreeFourTreeDelete(key)
                        else:
                            return False
                else:
                    self.left.twoThreeFourTreeDelete(key)
            elif self.root.getLength() == 3:    #Node is 4-node, delete in appropriate subtree
                if self.root.retrieve(0)[0].getKey() < key:
                    if self.root.retrieve(1)[0].getKey() < key:
                        if self.root.retrieve(2)[0].getKey() < key:
                            if self.right is not None:
                                return self.right.twoThreeFourTreeDelete(key)
                            else:
                                return False
                        else:
                            if self.rightmid is not None:
                                return self.rightmid.twoThreeFourTreeDelete(key)
                            else:
                                return False
                    else:
                        if self.leftmid is not None:
                            return self.leftmid.twoThreeFourTreeDelete(key)
                        else:
                            return False
                else:
                    if self.left is not None:
                        return self.left.twoThreeFourTreeDelete(key)
                    else:
                        return False
        else: #Node is 2-node
            self.__adjust() #Adjust the node
            return self.twoThreeFourTreeDelete(key) #Delete

    def __getInorderSuccesor(self, index):  #Returns inorder successor, adjusts every 2-node on path to inorder successor
        current = self
        if self.root.getLength() == 1:  #Set current appropriately for current node
            if index == 0:
                if self.right is not None:
                    current = self.right
        if self.root.getLength() == 2:
            if index == 0:
                if self.leftmid is not None:
                    current = self.leftmid
            if index == 1:
                if self.right is not None:
                    current = self.right
        if self.root.getLength() == 3:
            if index == 0:
                if self.leftmid is not None:
                    current = self.leftmid
            elif index == 1:
                if self.rightmid is not None:
                    current = self.rightmid
            elif index == 2:
                if self.right is not None:
                    current = self.right
        if current.root.getLength() == 1 and self.parent is not None:   #Adjust if current is 2-node
            #if current.left is not None or current.leftmid is not None or current.rightmid is not None or current.right is not None:
            current.__adjust()
        while current.left is not None: #Keep going left and adjust along the way
            while current.root.getLength() != 1 or self.parent is None:
                if current.left is not None:
                    current = current.left
                else:
                    break
            #if current.left is not None or current.leftmid is not None or current.rightmid is not None or current.right is not None:
            current.__adjust()
        io = current.root.retrieve(0)[0]    #Return the inorder successor
        current.root.delete(0)
        if current.root.getLength() == 0:
            if current == current.parent.left:
                current.parent.left = None
            elif current == current.parent.leftmid:
                current.parent.leftmid = None
            elif current == current.parent.rightmid:
                current.parent.rightmid = None
            elif current == current.parent.right:
                current.parent.right = None
        return io

    def __adjust(self): #Gets siblings with excess, redistributes if there are siblings with excess, fuses if there are none
        siblingwithexcess = self.__getSiblingWithExcess()
        if siblingwithexcess is not None:
            print(siblingwithexcess.root.retrieve(0)[0].getKey())
            self.__redistribute(siblingwithexcess)
        else:
            self.__fuse()

    def __fuse(self):   #Fuses different nodes
        if self.parent.root.getLength() == 1:   #2-node (if parent is root)
            if self == self.parent.left:
                self.root.insert(1, self.parent.root.retrieve(0)[0])
                self.root.insert(2, self.parent.right.root.retrieve(0)[0])
                self.leftmid = self.right       #Set appropriate subtrees
                self.rightmid = self.parent.right.left
                self.right = self.parent.right.right
                self.parent = None
            else:
                self.root.insert(0, self.parent.root.retrieve(0)[0])
                self.root.insert(0, self.parent.left.root.retrieve(0)[0])
                self.rightmid = self.left
                self.leftmid = self.parent.left.right
                self.left = self.parent.left.left
        else:
            if self == self.parent.left:    #Left subtree
                self.root.insert(1, self.parent.root.retrieve(0)[0])
                self.parent.root.delete(0)
                self.root.insert(2, self.parent.leftmid.root.retrieve(0)[0])    #Get elements from root and sibling
                self.leftmid = self.right       #Reconnect subtrees and delete duplicates
                self.rightmid = self.parent.leftmid.left
                self.right = self.parent.leftmid.right
                self.parent.leftmid = self.parent.rightmid
                self.parent.leftmid = None
            elif self == self.parent.leftmid:   #Leftmid subtree, same algorithm as above
                self.root.insert(0, self.parent.root.retrieve(0)[0])
                self.parent.root.delete(0)
                self.root.insert(0, self.parent.left.root.retrieve(0)[0])
                self.rightmid = self.left
                self.left = self.parent.left.left
                self.leftmid = self.parent.left.right
                self.parent.left = self.parent.leftmid
                self.parent.leftmid = self.parent.rightmid
                self.parent.rightmid = None
            elif self == self.parent.right and self.parent.root.getLength() == 2 or self == self.parent.rightmid and self.parent.root.getLength() == 3: #Right or rightmid subtree, idem
                self.root.insert(0, self.parent.root.retrieve(1)[0])
                self.parent.root.delete(1)
                self.root.insert(0, self.parent.leftmid.root.retrieve(0)[0])
                self.rightmid = self.left
                self.left = self.parent.leftmid.left
                self.leftmid = self.parent.leftmid.right
                self.parent.leftmid = self.parent.rightmid
                self.parent.rightmid = None
            elif self == self.parent.right and self.parent.root.getLength() == 3:   #Right subtree, idem
                self.root.insert(0, self.parent.root.retrieve(2)[0])
                self.parent.root.delete(2)
                self.root.insert(0, self.parent.rightmid.root.retrieve(0)[0])
                self.rightmid = self.left
                self.left = self.parent.rightmid.left
                self.leftmid = self.parent.rightmid.right
                self.parent.leftmid = self.parent.rightmid
                self.parent.rightmid = None


    def __redistribute(self, siblingwithexcess):    #Redistributes TreeItems, this is different for every subtree of every node length and for every sibling direction (a lot of different cases)
        if self.parent.root.getLength() == 1:   #2-node (root)
            if self == self.parent.left:
                self.root.insert(1, self.parent.root.retrieve(0)[0])    #Get item from root and from sibling with excess, delete items in root and sibling (indexes are different for every case)
                self.parent.root.delete(0)
                self.parent.root.insert(0, siblingwithexcess.root.retrieve(0)[0])
                siblingwithexcess.root.delete(0)
                self.leftmid = self.right
                self.right = siblingwithexcess.left
                if siblingwithexcess.rightmid is not None:
                    siblingwithexcess.leftmid = siblingwithexcess.rightmid
                    siblingwithexcess.rightmid = None
                else:
                    siblingwithexcess.left = siblingwithexcess.leftmid
                    siblingwithexcess.leftmid = None
            elif self == self.parent.right:
                self.root.insert(0, self.parent.root.retrieve(0)[0])
                self.parent.root.delete(0)
                self.parent.root.insert(0, siblingwithexcess.root.retrieve(siblingwithexcess.root.getLength() - 1)[0])
                siblingwithexcess.root.delete(siblingwithexcess.root.getLength() - 1)
                self.leftmid = self.left
                self.left = siblingwithexcess.right
                if siblingwithexcess.rightmid is not None:
                    siblingwithexcess.right = siblingwithexcess.rightmid
                    siblingwithexcess.rightmid = None
                else:
                    siblingwithexcess.right = siblingwithexcess.leftmid
                    siblingwithexcess.leftmid = None
        if self.parent.root.getLength() == 2:   #3-node
            if self == self.parent.left:    #Node is left
                self.root.insert(1, self.parent.root.retrieve(0)[0])
                self.parent.root.delete(0)
                self.parent.root.insert(1, siblingwithexcess.root.retrieve(0)[0])
                siblingwithexcess.root.delete(0)
            elif self == self.parent.leftmid: #Node is mid
                if siblingwithexcess == self.parent.right:  #Sibling is right
                    self.root.insert(1, self.parent.root.retrieve(1)[0])
                    self.parent.root.delete(1)
                    self.parent.root.insert(1, siblingwithexcess.root.retrieve(0)[0])
                    siblingwithexcess.root.delete(0)
                else:   #Sibling is left
                    self.root.insert(0, self.parent.root.retrieve(0)[0])
                    self.parent.root.delete(0)
                    self.parent.root.insert(0, siblingwithexcess.root.retrieve(siblingwithexcess.root.getLength() - 1)[0])
                    siblingwithexcess.root.delete(siblingwithexcess.root.getLength() - 1)
            else:   #Node is right
                self.root.insert(0, self.parent.root.retrieve(1)[0])
                self.parent.root.delete(1)
                self.parent.root.insert(0, siblingwithexcess.root.retrieve(siblingwithexcess.root.getLength() - 1)[0])
                siblingwithexcess.root.delete(siblingwithexcess.root.getLength - 1)
        elif self.parent.root.getLength() == 3: #4-node
            if self == self.parent.left:
                self.root.insert(1, self.parent.root.retrieve(0)[0])
                self.parent.root.delete(0)
                self.parent.root.insert(1, siblingwithexcess.root.retrieve(0)[0])
                siblingwithexcess.root.delete(0)
            elif self == self.parent.leftmid:
                if siblingwithexcess == self.parent.rightmid:  # Sibling is right
                    self.root.insert(1, self.parent.root.retrieve(1)[0])
                    self.root.delete(1)
                    self.parent.root.insert(1, siblingwithexcess.root.retrieve(0)[0])
                    siblingwithexcess.root.delete(siblingwithexcess.root.getLength() - 1)
                else:   # Sibling is left
                    self.root.insert(0, self.parent.root.retrieve(0)[0])
                    self.root.delete(0)
                    self.parent.root.insert(0, siblingwithexcess.root.retrieve(0)[0])
                    siblingwithexcess.root.delete(siblingwithexcess.root.getLength() - 1)
            elif self == self.parent.rightmid:
                if siblingwithexcess == self.parent.right:  #Sibling is right
                    self.root.insert(1, self.parent.root.retrieve(2)[0])
                    self.root.delete(2)
                    self.parent.root.insert(2, siblingwithexcess.root.retrieve(0)[0])
                    siblingwithexcess.root.delete(siblingwithexcess.root.getLength() - 1)
                else:   # Sibling is left
                    self.root.insert(0, self.parent.root.retrieve(1)[0])
                    self.root.delete(1)
                    self.parent.root.insert(1, siblingwithexcess.root.retrieve(siblingwithexcess.root.getLength() - 1)[0])
                    siblingwithexcess.root.delete(siblingwithexcess.root.getLength() - 1)
            else:   #Node is right
                self.root.insert(0, self.parent.root.retrieve(2)[0])
                self.root.delete(2)
                self.parent.root.insert(2, siblingwithexcess.root.retrieve(siblingwithexcess.root.getLength() - 1)[0])

    def __getSiblingWithExcess(self):   #Returns a sibling if it has excess items (more than one)
        if self.parent is None: #root
            return None
        leftlength = 0
        leftmidlength = 0
        rightmidlength = 0
        rightlength = 0
        if self.parent.left is not None:   #Get length of children
            leftlength = self.parent.left.root.getLength()
        if self.parent.leftmid is not None:
            leftmidlength = self.parent.leftmid.root.getLength()
        if self.parent.rightmid is not None:
            rightmidlength = self.parent.rightmid.root.getLength()
        if self.parent.right is not None:
            rightlength = self.parent.right.root.getLength()
        if self == self.parent.left:        #Check if sibling has more than one item (for every length and subtree)
            if self.parent.root.getLength() == 1:
                if rightlength > 1:
                    return self.parent.right
            elif self.parent.root.getLength() == 2 or self.parent.root.getLength() == 3:
                if leftmidlength > 1:
                    return self.parent.leftmid
        elif self == self.parent.leftmid:
            if self.parent.root.getLength() == 2:
                if leftlength > 1:
                    return self.parent.left
                if rightlength > 1:
                    return self.parent.rightmid
            elif self.parent.root.getLength() == 3:
                if leftlength > 1:
                    return self.parent.left
                if rightmidlength > 1:
                    return self.parent.rightmid
        elif self == self.parent.rightmid:
            if leftmidlength > 1:
                return self.parent.leftmid
            if rightlength > 1:
                return self.parent.right
        elif self == self.parent.right:
            if self.parent.root.getLength() == 1:
                if leftlength > 1:
                    return self.parent.left
            elif self.parent.root.getLength() == 2:
                if leftmidlength > 1:
                    return self.parent.leftmid
            elif self.parent.root.getLength() == 3:
                if rightmidlength > 1:
                    return self.parent.rightmid
        return None

    def twoThreeFourTreeRetrieve(self, key):
        """
        Returns TreeItem with given key from TwoThreeFourTree
        :param TreeItem: TreeItem to be retrieved
        :return: TreeItem (None if it's not in TwoThreeFourTree) and True/False indicating if it was found or not
        >>> t = TwoThreeFourTree()
        >>> t.twoThreeFourTreeInsert(TreeItem("Test", 5))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 2", 7))
        True
        >>> t.twoThreeFourTreeRetrieve(5)
        >>> t.twoThreeFourTreeRetrieve(7)
        >>> t.twoThreeFourTreeRetrieve(9)
        False
        """
        for i in range(self.root.getLength()):
            if self.root.retrieve(i)[0].getKey() == key:
                return self.root.retrieve(i)[0], True
        if self.root.getLength() == 1:
            if self.root.retrieve(0)[0].getKey() < key:
                if self.right is not None:
                    return self.right.twoThreeFourTreeRetrieve(key)
            else:
                if self.left is not None:
                    return self.left.twoThreeFourTreeRetrieve(key)
        elif self.root.getLength() == 2:
            if self.root.retrieve(0)[0].getKey() < key:
                if self.root.retrieve(1)[0].getKey() < key:
                    if self.right is not None:
                        return self.right.twoThreeFourTreeRetrieve(key)
                else:
                    if self.leftmid is not None:
                        return self.leftmid.twoThreeFourTreeInsert(key)
            else:
                if self.left is not None:
                    return self.left.twoThreeFourTreeRetrieve(key)
        elif self.root.getLength() == 3:
            if self.root.retrieve(0)[0].getKey() < key:
                if self.root.retrieve(1)[0].getKey() < key:
                    if self.root.retrieve(2)[0].getKey() < key:
                        if self.right is not None:
                            return self.right.twoThreeFourTreeRetrieve(key)
                    else:
                        if self.rightmid is not None:
                            return self.rightmid.twoThreeFourTreeRetrieve(key)
                else:
                    if self.leftmid is not None:
                        return self.leftmid.twoThreeFourTreeRetrieve(key)
            else:
                if self.left is not None:
                    return self.left.twoThreeFourTreeRetrieve(key)
        return None, False

    def inorderTraverse(self):
        """
        Traverse elements in TwoThreeFourTree in order
        :return: List with elements in order
        >>> t = TwoThreeFourTree()
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 5", 5))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 2", 2))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 9", 9))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 7", 7))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 11", 11))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 1", 1))
        True
        >>> t.twoThreeFourTreeInsert(TreeItem("Test 3", 3))
        True
        >>> t.inorderTraverse()
        ['Test 1', 'Test 2', 'Test 3', 'Test 5', 'Test 7', 'Test 9', 'Test 11']
        >>> t.getTreeLength()
        7
        """
        traverseList = []
        if self.root.getLength() == 1:  #1-node
            if self.left is not None:
                traverseList = self.left.inorderTraverse()
            traverseList.append(self.root.retrieve(0)[0].getItem())
            if self.right is not None:
                traverseList = traverseList + self.right.inorderTraverse()
            return traverseList
        elif self.root.getLength() == 2:    #2-node
            if self.left is not None:
                traverseList = self.left.inorderTraverse()
            traverseList.append(self.root.retrieve(0)[0].getItem())
            if self.leftmid is not None:
                traverseList = traverseList + self.leftmid.inorderTraverse()
            traverseList.append(self.root.retrieve(1)[0].getItem())
            if self.right is not None:
                traverseList = traverseList + self.right.inorderTraverse()
            return traverseList
        elif self.root.getLength() == 3:    #3-node
            if self.left is not None:
                traverseList = self.left.inorderTraverse()
            traverseList.append(self.root.retrieve(0)[0].getItem())
            if self.leftmid is not None:
                traverseList = traverseList + self.leftmid.inorderTraverse()
            traverseList.append(self.root.retrieve(1)[0].getItem())
            if self.rightmid is not None:
                traverseList = traverseList + self.rightmid.inorderTraverse()
            traverseList.append(self.root.retrieve(2)[0].getItem())
            if self.right is not None:
                traverseList = traverseList + self.right.inorderTraverse()
            return traverseList

    def print(self):
        """
        Function for testing purposes, prints elements of all items in TwoThreeFourTree in order
        """
        for i in self.inorderTraverse():
            print(i)

    def getTreeLength(self):
        """
        Returns amount of elements in TwoThreeFourTree
        :return: amount of elements
        """
        return len(self.inorderTraverse())
