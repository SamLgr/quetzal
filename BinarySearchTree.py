from TreeItem import TreeItem
from CircularLinkedList import CircularLinkedList

class BinarySearchTree:
    def __init__(self):
        self.root = CircularLinkedList()
        self.left = None
        self.right = None

    def __del__(self):
        self.root = CircularLinkedList()
        self.left = None
        self.right = None

    def isEmpty(self):
        """
        Returns if binary search tree is empty.
        :return: True if empty, False if not empty
        """
        return self.root.isEmpty()

    def getTreeLength(self):
        """
        Returns length of binary search tree.
        :return: length of binary search tree
        """
        return len(self.inorderTraverse())

    def searchTreeInsert(self, TreeItem):
        """
        Inserts tree item in binary search tree.
        :param TreeItem: tree item to be inserted
        :return: bool indicating if insert was successful
        """
        if self.isEmpty():
            return self.root.append(TreeItem)
        elif TreeItem.getKey() < self.root.first().getKey():
            if self.left is None:
                self.left = BinarySearchTree()
            return self.left.searchTreeInsert(TreeItem)
        elif TreeItem.getKey() > self.root.first().getKey():
            if self.right is None:
                self.right = BinarySearchTree()
            return self.right.searchTreeInsert(TreeItem)

    def searchTreeDelete(self, key):
        """
        Deletes tree item associated with given key from binary search tree.
        :param key: given key of tree item to be deleted
        :return: bool indicating if delete was successful
        >>> b = BinarySearchTree()
        >>> b.searchTreeInsert(TreeItem("Test", 5))
        True
        >>> b.searchTreeInsert(TreeItem("Test Links", 2))
        True
        >>> b.searchTreeInsert(TreeItem("Test Rechts", 9))
        True
        >>> b.searchTreeInsert(TreeItem("Test Rechts Rechts", 11))
        True
        >>> b.searchTreeInsert(TreeItem("Test Rechts Links", 7))
        True
        >>> b.searchTreeDelete(9)
        True
        >>> b.searchTreeDelete(4)
        False
        >>> b.searchTreeRetrieve(9)
        (None, False)
        """
        parent = None
        tree = self
        left = False
        right = False
        while key != tree.root.first().getKey():
            if key < tree.root.first().getKey():
                parent = tree
                tree = tree.left
                left = True
                right = False
            elif key > tree.root.first().getKey():
                parent = tree
                tree = tree.right
                right = True
                left = False
            if tree is None:
                return False
        treeToDelete = tree
        if treeToDelete.left is None and treeToDelete.right is None:
            if parent is None:
                self.root = CircularLinkedList()
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
        Returns tree item associated with the given key.
        :param key: given key of binary search tree to be retrieved
        :return: tree item associated with given key, bool indicating if retrieve was successful
        >>> b = BinarySearchTree()
        >>> b.searchTreeInsert(TreeItem("Test", 5))
        True
        >>> b.searchTreeInsert(TreeItem("Test Links", 2))
        True
        >>> b.searchTreeInsert(TreeItem("Test Rechts", 9))
        True
        >>> b.searchTreeRetrieve(5)
        """
        if self.root.isEmpty():
            return None, False
        elif key == self.root.first().getKey():
            if self.root.getLength() == 1:
                return self.root.first(), True
            else:
                return self.root, True
        elif key < self.root.first().getKey():
            if self.left is not None:
                return self.left.searchTreeRetrieve(key)
        elif key > self.root.first().getKey():
            if self.right is not None:
                return self.right.searchTreeRetrieve(key)
        return None, False

    def inorderTraverse(self):
        """
        Returns all items in binary search tree in sorted search key order.
        :return: List containing all items in binary search tree
        >>> b = BinarySearchTree()
        >>> b.searchTreeInsert(TreeItem("Test 5", 5))
        True
        >>> b.searchTreeInsert(TreeItem("Test 2", 2))
        True
        >>> b.searchTreeInsert(TreeItem("Test 9", 9))
        True
        >>> b.searchTreeInsert(TreeItem("Test 7", 7))
        True
        >>> b.searchTreeInsert(TreeItem("Test 11", 11))
        True
        >>> b.searchTreeInsert(TreeItem("Test 1", 1))
        True
        >>> b.searchTreeInsert(TreeItem("Test 3", 3))
        True
        >>> b.inorderTraverse()
        ['Test 1', 'Test 2', 'Test 3', 'Test 5', 'Test 7', 'Test 9', 'Test 11']
        """
        traverseList = []
        if self.left is not None:
            traverseList = self.left.inorderTraverse()
        for i in range(self.root.getLength()):
            traverseList.append(self.root.retrieve(i)[0].getItem())
        if self.right is not None:
            traverseList = traverseList + self.right.inorderTraverse()
        return traverseList

    def print(self):
        """
        Function for testing purposes, prints out all items of binary search tree in sorted manner.
        :return:
        >>> b = BinarySearchTree()
        >>> b.searchTreeInsert(TreeItem("Test 5", 5))
        True
        >>> b.searchTreeInsert(TreeItem("Test 2", 2))
        True
        >>> b.searchTreeInsert(TreeItem("Test 9", 9))
        True
        >>> b.searchTreeInsert(TreeItem("Test 7", 7))
        True
        >>> b.searchTreeInsert(TreeItem("Test 11", 11))
        True
        >>> b.searchTreeInsert(TreeItem("Test 1", 1))
        True
        >>> b.searchTreeInsert(TreeItem("Test 3", 3))
        True
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
            print(i)
