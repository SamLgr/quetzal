"""
Testing Hashmap + documentation

#Calling constructor with type 3 (Separate chaining):
#and max size 50
>>> hmap = Hashmap(3, 50)

#Get length of hashmap:
>>> hmap.getLength()
0

#We want to add the string "A" in the Hashmap, so use:
#an MapObject to do so
>>> toAdd = MapObject(1, "A")
>>> hmap.insert(toAdd)
True
>>> toAdd = MapObject(2, "B")
>>> hmap.insert(toAdd)
True
>>> toAdd = MapObject(2, "X")
>>> hmap.insert(toAdd)
True
>>> toAdd = MapObject(4, "C")
>>> hmap.insert(toAdd)
True
>>> toAdd = MapObject(5, "D")
>>> hmap.insert(toAdd)
True
>>> toAdd = MapObject(5, "E")
>>> hmap.insert(toAdd)
True

#Getting first element:
>>> hmap.begin()
'A'

#Getting last element:
>>> hmap.end()
'E'

#Erase an element:
#Making MapObject with data we want to delete
>>> toDelete = MapObject(5, "E")
>>> hmap.erase(toDelete)
True

#Now last element should be 'D'
>>> hmap.end()
'D'

#Find by hash:
#Hashing a key
>>> key = 2
>>> hash = hmap.hash(key)
>>> x = hmap.findByHash(hash)
>>> print(hmap.fetch(x, 0))
B

#Retrieve by key:
>>> key = 4
>>> hmap.fetch(hmap.retrieve(key), 0)
'C'

#Getting length:
>>> hmap.getLength()
5

#Traversing hashmap:
>>> hmap.traverse()
['A', 'B', 'X', 'C', 'D']

#Display hashmap:
#>>> hmap.print()

#Destroying hashmap:
>>> hmap.destroyHashmap()
True

"""

#from CircularLinkedList import CircularLinkedList as List
from DoubleList import DoubleList as List
from DoubleNode import Node
import math

#MapObject
#Used to add and delete objects
#in hashmap
class MapObject:
    key = 0
    myObject = None
    
    #Constructor
    #:param key: int -> hash(key) to insert object in hashmap
    #:param myObject: Object -> Object to insert
    def __init__(self, key, myObject):
        self.key = key
        self.myObject = myObject

        return None

#Hashmap
class Hashmap:
    v = []
    max_size = 50
    myType = 1

    #Constructor
    #:param myType: Int =
    #   1 -> Linear probing
    #   2 -> Quadratic probing
    #   3 -> Separate chaining
    #:param max_size: Int -> Maximum allowed size of Hashmap
    def __init__(self, myType=None, max_size=0):
        self.myType = myType
        self.max_size = max_size
        self.v = [None] * max_size
        
        return None

    #Returns first element in hashmap
    def begin(self):
        i = 0
        if self.myType == 3:
            while self.v[i] == None:
                i+=1
            return self.v[i].first().item

        while self.v[i] == None:
            i+=1
        return self.v[i]

    #Returns last element in hashmap
    def end(self):
        i = len(self.v) -1
        if self.myType == 3:
            while self.v[i] == None:
                i-=1
            return self.v[i].last().item

        while self.v[i] == None:
            if i == 0: return None
            i-=1
        return self.v[i]

    #Inserts object 'toAdd' in hashmap
    #:param toAdd: MapObject -> Object to add
    #:return bool: True if succesful
    def insert(self, toAdd):
        #Setting variables
        key = toAdd.key
        objectToAdd = toAdd.myObject

        #If hash is bigger than allowed max_size, modulo it
        if self.hash(key) > self.max_size:
            newToAdd = MapObject(key % self.max_size, objectToAdd)
            return insert(newToAdd)
        

        #Separate chaining
        if self.myType == 3:
            if self.v[self.hash(key)] == None:
                l = List()
                node = Node(objectToAdd)
                l.append(node)
            else:
                l = self.v[self.hash(key)]
                node = Node(objectToAdd)
                l.append(node)

            self.v[self.hash(key)] = l

            return True

        #Probing
        if self.v[self.hash(key)] != None:
            i = self.hash(key)

            #Linear probing
            if self.myType == 1:
                while (self.v[i] != None):
                    i+=1
                self.v[i] = objectToAdd

            #Quadratic probing
            if self.myType == 2:
                while (self.v[i] != None):
                    i+=1
                    i = i ** 2 % self.max_size
                self.v[i] = objectToAdd
            
            return True

        #No probing or chaining needed, normal insert
        self.v[self.hash(key)] = objectToAdd
        return True
        

    #Deletes object 'toAdd' from hashmap
    #:param toAdd: MapObject -> Object to delete
    #:return bool: True if succesful
    def erase(self, toErase):
        key = toErase.key
        d = toErase.myObject

        if self.myType == 3:
            sum = 0
            for i in self.v[self.hash(key)].getItems():
                if i.item == d:
                    self.v[self.hash(key)].delete(sum)

                sum += 1
            return True
       
        if self.myType == 2:
            sum = 0
            for i in self.v:
                if i == d:
                    del self.v[sum]
                sum += 1
            return True

        if self.myType == 1:
            sum = 0    
            for i in self.traverse():
                if i != d:
                    sum += 1
            
            iterator = 0
            for i in self.v:
                if i != None:
                    sum -= 1
                
                if sum == 0:
                    del self.v[iterator +1]
                    return True
                
                iterator += 1
                    
            return False

    #Returns object by it's hash
    #:param h: Hash -> hash(key) to find mapped object
    #:return Object: -> Object mapped to hash
    def findByHash(self, h):
        if self.myType == 3:
            l = []

            for i in self.v[h].getItems():
                l.append(i.getItem())
            return l
        return self.v[h]

    #Hashes a key
    #:param key: Int -> Key to hash
    #:return int: hash(key) -> Hashed key
    def hash(self, key):
        return int(key + (key/2) + math.sqrt(key) % (key/2))

    #Return object by key
    #:param key: Int -> Return object mapped to this key
    #:return Object: Object mapped to key
    def retrieve(self, key):
        hash = self.hash(key)
        return self.findByHash(hash)


    #Prints out whole hashmap
    def print(self):
        if self.myType == 3:
            sum = 0
            for i in self.v:
                if i == None:
                    sum += 1
                    print(str(sum) + ".\t" + str(None))
                else:
                    l = i.getItems()
                    sum += 1
                    print(str(sum) + ".\t")
                    for j in l:
                        print("\t-> " + str(j.item))
        else:
            sum = 0
            for i in self.v:
                sum+=1
                print(str(sum) + ".\t" + str(i))

    #Returns the length of the Hashmap
    #:return int: returns the length
    def getLength(self):
        sum = 0
        for i in self.v:
            if self.myType == 3:
                if i != None:
                    for j in i.getItems():
                        if j != None:
                            sum += 1
            
            else:
                if i != None: sum += 1

        return sum

    #Returns if hashmap is empty
    #:return bool: True if empty
    def isEmpty(self):
        if self.getLength() == 0:
            return True 
        return False

    #Traverses the whole hashmap
    #:return list: List of all elements in the hashmap
    def traverse(self):
        traverseList = []
        
        for i in self.v:

            if i != None:
                if self.myType == 3:
                    for j in i.getItems():
                        traverseList.append(j.item)
                else:
                    traverseList.append(i)

        return traverseList

    #Deletes the whole Hashmap
    #:return bool: True if succesful
    def destroyHashmap(self):
        del self.v
        return True


    ################
    #Ignore this function, this is just
    #for documentation purposes!
    #Makes sure we can switch between probing and chaining
    #in documentation
    def fetch(self, obj=None, n=0):
        if self.myType == 3:
            return obj[n]

        else:
            return obj


    def dotDebug(self):
        myStr = """
            digraph  { 
             mindist=0;
             ranksep=0;
             nodesep=0;

             node[shape=box,margin="0,0",width=1, height=0.5];
             edge [style=invis];

             Hashmap[width=2];
             Hashmap -> Hash;
             Hashmap -> Value;
        """

        firstDone = False
        for i in range(0, len(self.v)):
            if hmap.retrieve(i) == None: continue

            key = i
            value = hmap.retrieve(key)            

            if not firstDone:
                prevKey = "Hash"
                prevValue = "Value"
                firstDone = True
            else:
                prevKey = i - 1
                prevValue = hmap.retrieve(prevKey)

            myStr += str(prevKey) + " -> " + str(key) + ';\n'
            myStr += str(prevValue) + " -> " + str(value) + ';\n'

        myStr += "}"
        print(myStr)

