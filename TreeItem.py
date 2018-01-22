class TreeItem:
    # Constructor
    # item: Item to be inserted in tree
    # key: Key associated with given item
    def __init__(self, item, key):
        self.item = item
        self.key = key

    # Returns item in tree item
    def getItem(self):
        return self.item

    # Returns key in tree item
    def getKey(self):
        return self.key
