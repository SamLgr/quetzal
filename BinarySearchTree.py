from TreeItem import TreeItem

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def __del__(self):
        self.root = None
        self.left = None
        self.right = None

    def isEmpty(self):
        """
        Tests if BinarySearchTree is empty
        :return: True if empty, False if not empty
        """
        return self.root is None

    def getTreeLength(self):
        """
        Returns length of BinarySearchTree.
        :return: length
        """
        return len(self.inorderTraverse())

    def searchTreeInsert(self, TreeItem):
        """
        Inserts TreeItem in BinarySearchTree
        :param TreeItem: TreeItem to be inserted
        :return: False if key is already present
        """
        if self.isEmpty():
            self.root = TreeItem
        elif TreeItem.getKey() < self.root.getKey():
            if self.left is None:
                self.left = BinarySearchTree()
            self.left.searchTreeInsert(TreeItem)
        elif TreeItem.getKey() > self.root.getKey():
            if self.right is None:
                self.right = BinarySearchTree()
            self.right.searchTreeInsert(TreeItem)
        else:
            return False

    def searchTreeDelete(self, key):
        """
        Deletes TreeItem in BinarySearchTree
        :param key: given key of TreeItem to be deleted
        :return: False if key is not in BinarySearchTree
        >>> b = BinarySearchTree()
        >>> b.searchTreeInsert(TreeItem("Test", 5))
        >>> b.searchTreeInsert(TreeItem("Test Links", 2))
        >>> b.searchTreeInsert(TreeItem("Test Rechts", 9))
        >>> b.searchTreeInsert(TreeItem("Test Rechts Rechts", 11))
        >>> b.searchTreeInsert(TreeItem("Test Rechts Links", 7))
        >>> b.searchTreeDelete(9)
        True
        >>> b.searchTreeDelete(4)
        False
        >>> b.searchTreeRetrieve(9)
        False
        """
        parent = None
        tree = self
        left = False
        right = False
        while key != tree.root.getKey():
            if key < tree.root.getKey():
                parent = tree
                tree = tree.left
                left = True
                right = False
            elif key > tree.root.getKey():
                parent = tree
                tree = tree.right
                right = True
                left = False
            if tree is None:
                return False
        treeToDelete = tree
        if treeToDelete.left is None and treeToDelete.right is None:
            if parent is None:
                self.root = None
            elif left:
                parent.left = None
            elif right:
                parent.right = None
            return True
        elif treeToDelete.left is None:
            if parent is None:
                treeToDelete.root = treeToDelete.right.root
                treeToDelete.left = treeToDelete.right.left
                treeToDelete.right = treeToDelete.right.right
            elif left:
                parent.left = treeToDelete.right
            elif right:
                parent.right = treeToDelete.right
            return True
        elif treeToDelete.right is None:
            if parent is None:
                treeToDelete.root = treeToDelete.left.root
                treeToDelete.left = treeToDelete.left.left
                treeToDelete.right = treeToDelete.left.right
            elif left:
                parent.left = treeToDelete.left
            elif right:
                parent.right = treeToDelete.left
            return True
        else:
            tree = treeToDelete.right   #Get inorder successor
            parent = None
            while tree.left is not None:
                parent = tree
                tree = tree.left
            treeToDelete.root = tree.root
            if parent is None:
                treeToDelete.right = treeToDelete.right.right
            else:
                if tree.right is not None:
                    parent.left = tree.right
                else:
                    parent.left = None
            return True

    def searchTreeRetrieve(self, key):
        """
        Returns BinarySearchTree with the given key
        :param key: given key of BinarySearchTree to be retrieved
        :return: BinarySearchTree or False if key is not in BinarySearchTree
        >>> b = BinarySearchTree()
        >>> b.searchTreeInsert(TreeItem("Test", 5))
        >>> b.searchTreeInsert(TreeItem("Test Links", 2))
        >>> b.searchTreeInsert(TreeItem("Test Rechts", 9))
        >>> b.searchTreeRetrieve(2)
        """
        if key == self.root.getKey():
            return self
        elif key < self.root.getKey():
            if self.left is not None:
                return self.left.searchTreeRetrieve(key)
        elif key > self.root.getKey():
            if self.right is not None:
                return self.right.searchTreeRetrieve(key)
        return False

    def inorderTraverse(self):
        """
        Prints the inorderTraverse of BinarySearchTree
        :return: None
        >>> b = BinarySearchTree()
        >>> b.searchTreeInsert(TreeItem("Test 5", 5))
        >>> b.searchTreeInsert(TreeItem("Test 2", 2))
        >>> b.searchTreeInsert(TreeItem("Test 9", 9))
        >>> b.searchTreeInsert(TreeItem("Test 7", 7))
        >>> b.searchTreeInsert(TreeItem("Test 11", 11))
        >>> b.searchTreeInsert(TreeItem("Test 1", 1))
        >>> b.searchTreeInsert(TreeItem("Test 3", 3))
        >>> b.inorderTraverse()
        """
        traverseList = []
        if self.left is not None:
            traverseList = self.left.inorderTraverse()
        traverseList.append(self.root)
        if self.right is not None:
            traverseList = traverseList + self.right.inorderTraverse()
        return traverseList

    def print(self):
        """
        Prints out all items of BinarySearchTree in sorted manner
        :return:
        >>> b = BinarySearchTree()
        >>> b.searchTreeInsert(TreeItem("Test 5", 5))
        >>> b.searchTreeInsert(TreeItem("Test 2", 2))
        >>> b.searchTreeInsert(TreeItem("Test 9", 9))
        >>> b.searchTreeInsert(TreeItem("Test 7", 7))
        >>> b.searchTreeInsert(TreeItem("Test 11", 11))
        >>> b.searchTreeInsert(TreeItem("Test 1", 1))
        >>> b.searchTreeInsert(TreeItem("Test 3", 3))
        >>> b.print()
        Test 1
        Test 2
        Test 3
        Test 5
        Test 7
        Test 9
        Test 11
        """
        for i in self.inorderTraverse():
            print(i.getItem())
