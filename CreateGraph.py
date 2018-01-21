import graphviz as gv

from BinarySearchTree import BinarySearchTree
from TreeItem import TreeItem
from TwoThreeFourTree import TwoThreeFourTree
from CircularLinkedList import CircularLinkedList
from Stack import Stack

def readFile():
    file = open("input.txt", "r")       # opens file
    command = file.readline()
    if "type" in command:
        if "bst" in command:        # creates BSTree
            b = BinarySearchTree()
            command = file.readline()
            while command is not None:
                if len(command.strip()) == 0:
                    break
                elif "insert" in command:       # inserts in BSTree
                    number = int(command.split()[1])
                    b.searchTreeInsert(TreeItem(str(number), number))
                    command = file.readline()
                elif "delete" in command:       # deletes in BSTree
                    number = int(command.split()[1])
                    b.searchTreeDelete(number)
                    command = file.readline()
                elif "print" in command:        # gives DOT-language of BSTree
                    createDotFileBST(b)
                    command = file.readline()
                    readFile()
        elif "234" in command:      # creates 234-Tree
            t = TwoThreeFourTree()
            command = file.readline()
            while command is not None:
                if len(command.strip()) == 0:
                    break
                elif "insert" in command:       # inserts in 234-Tree
                    number = int(command.split()[1])
                    t.twoThreeFourTreeInsert(TreeItem(str(number), number))
                    command = file.readline()
                elif "delete" in command:       # deletes in 234-Tree
                    number = int(command.split()[1])
                    t.twoThreeFourTreeDelete(number)
                    command = file.readline()
                elif "print" in command:        # gives DOT-language of 234-Tree
                    createDotFileTTFT(t)
                    command = file.readline()
        elif "ll" in command:
            l = CircularLinkedList()
            command = file.readline()
            while command is not None:
                if len(command.strip()) == 0:
                    break
                elif "insert" in command:
                    index = int(command.split()[1])
                    number = int(command.split()[2])
                    l.insert(index, number)
                    command = file.readline()
                elif "delete" in command:
                    index = int(command.split()[1])
                    l.delete(index)
                    command = file.readline()
                elif "print" in command:
                    createDotFileLL(l)
                    command = file.readline()
        elif "stack" in command:
            s = Stack()
            command = file.readline()
            while command is not None:
                if len(command.strip()) == 0:
                    break
                elif "push" in command:
                    number = int(command.split()[1])
                    s.push(number)
                    command = file.readline()
                elif "pop" in command:
                    s.pop()
                    command = file.readline()
                elif "print" in command:
                    createDotFileS(s)
                    command = file.readline()

def createDotFileBST(b):
    bg = gv.Graph(format='svg')     # create graph and add nodes
    bg.node(str(b.root.getKey()))
    addNodesBST(b, bg)
    print(bg.source)

def addNodesBST(b, bg):     # add nodes and edges for every node in BST
    if b.left is None:
        bg.node('', style='invisible')
        bg.edge(str(b.root.getKey()), '', style='invis')
    else:
        bg.node(str(b.left.root.getKey()))
        bg.edge(str(b.root.getKey()), str(b.left.root.getKey()))
        addNodesBST(b.left, bg)
    if b.right is None:
        bg.node('', style='invisible')
        bg.edge(str(b.root.getKey()), '', style='invis')
    else:
        bg.node(str(b.right.root.getKey()))
        bg.edge(str(b.root.getKey()), str(b.right.root.getKey()))
        addNodesBST(b.right, bg)

def createDotFileTTFT(t):       # create graph and add nodes
    tg = gv.Graph(format='svg')
    word = ""
    for i in range(t.root.getLength()):
        word += str(t.root.retrieve(i)[0].getKey())
        if i < t.root.getLength() - 1:
            word += " | "
    tg.node(str(t.root.retrieve(0)[0].getKey()), label=word)
    addNodesTTFT(t, tg)
    print(tg.source)

def addNodesTTFT(t, tg):        # add nodes and edges for every node in 234-Tree
    if t.left is None:
        tg.node('', style='invisible')
        tg.edge(str(t.root.retrieve(0)[0].getKey()), '', style='invis')
    else:
        word = ""
        for i in range(t.left.root.getLength()):
            word += str(t.left.root.retrieve(i)[0].getKey())
            if i < t.left.root.getLength() - 1:
                word += " | "
        tg.node(str(t.left.root.retrieve(0)[0].getKey()), label=word)
        tg.edge(str(t.root.retrieve(0)[0].getKey()), str(t.left.root.retrieve(0)[0].getKey()))
        addNodesTTFT(t.left, tg)
    if t.leftmid is None:
        tg.node('', style='invisible')
        tg.edge(str(t.root.retrieve(0)[0].getKey()), '', style='invis')
    else:
        word = ""
        for i in range(t.leftmid.root.getLength()):
            word += str(t.leftmid.root.retrieve(i)[0].getKey())
            if i < t.leftmid.root.getLength() - 1:
                word += " | "
        tg.node(str(t.leftmid.root.retrieve(0)[0].getKey()), label=word)
        tg.edge(str(t.root.retrieve(0)[0].getKey()), str(t.leftmid.root.retrieve(0)[0].getKey()))
        addNodesTTFT(t.leftmid, tg)
    if t.rightmid is None:
        tg.node('', style='invisible')
        tg.edge(str(t.root.retrieve(0)[0].getKey()), '', style='invis')
    else:
        word = ""
        for i in range(t.rightmid.root.getLength()):
            word += str(t.rightmid.root.retrieve(i)[0].getKey())
            if i < t.rightmid.root.getLength() - 1:
                word += " | "
        tg.node(str(t.rightmid.root.retrieve(0)[0].getKey()), label=word)
        tg.edge(str(t.root.retrieve(0)[0].getKey()), str(t.rightmid.root.retrieve(0)[0].getKey()))
        addNodesTTFT(t.rightmid, tg)
    if t.right is None:
        tg.node('', style='invisible')
        tg.edge(str(t.root.retrieve(0)[0].getKey()), '', style='invis')
    else:
        word = ""
        for i in range(t.right.root.getLength()):
            word += str(t.right.root.retrieve(i)[0].getKey())
            if i < t.right.root.getLength() - 1:
                word += " | "
        tg.node(str(t.right.root.retrieve(0)[0].getKey()), label=word)
        tg.edge(str(t.root.retrieve(0)[0].getKey()), str(t.right.root.retrieve(0)[0].getKey()))
        addNodesTTFT(t.right, tg)

def createDotFileLL(l):
    lg = gv.Digraph(format='svg', node_attr={'shape': 'record'}, graph_attr={'rankdir': 'LR'})
    current = l.head.getNext().getNext()
    for i in range(l.getLength()-1):
        lg.node(str(current.getItem()), label="{ <data> " + str(current.getItem()) + " | <ref>  }")
        lg.edge(str(current.getItem()) + ":ref:c", str(current.getNext().getItem()))
        current = current.getNext()
    lg.node(str(current.getItem()), label="{ <data> " + str(current.getItem()) + " | <ref>  }")
    lg.edge(str(current.getItem()) + ":ref:c", str(l.head.getNext().getNext().getItem()))
    lg.edge_attr.update(arrowhead='vee', arrowtail='dot', dir='both', tailclip='false')
    print(lg.source)

def createDotFileS(s):
    sg = gv.Digraph(format='svg', node_attr={'shape': 'record'}, graph_attr={'rankdir': 'LR'})
    sg.node(name="stack", label="", height="0.001", fixedsize="true")
    for item in s.getItems():
        sg.node(str(item), label=str(item))
        sg.node(name=str(item))
    print(sg.source)

if __name__ == '__main__':
    readFile()