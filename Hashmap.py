"""
Testing Hashmap + documentation

#Calling constructor with type 3 (Separate chaining)
#and max size 50
>>> hmap = Hashmap(3, 50)

#We want to add the string "A" in the Hashmap, so use
#an MapObject to do so
>>> toAdd = MapObject(1, "A")
>>> hmap.insert(toAdd)
True
>>> toAdd = MapObject(1, "B")
>>> hmap.insert(toAdd)
True
>>> toAdd = MapObject(2, "C")
>>> hmap.insert(toAdd)
True
>>> toAdd = MapObject(2, "D")
>>> hmap.insert(toAdd)
True
>>> toAdd = MapObject(2, "E")
>>> hmap.insert(toAdd)
True

#Getting first element
>>> hmap.begin()
'A'

#Getting last element
>>> hmap.end()
'E'

#Erase an element
#Making MapObject with data we want to delete
>>> toDelete = MapObject(2, "E")
>>> hmap.erase(toDelete)
True

#Now last element should be 'D'
>>> hmap.end()
'D'
"""

from DoubleList import DoubleList as List
from DoubleNode import Node


class MapObject:
    key = 0
    myObject = None
    
    def __init__(self, key, myObject):
        self.key = key
        self.myObject = myObject

        return None

class Hashmap:
    v = []
    max_size = 0
    myType = 0

    #Constructor
    #param myType: Int =
    #   1 -> Linear probing
    #   2 -> Quadratic probing
    #   3 -> Separate chaining
    def __init__(self, myType=None, max_size=0):
        self.myType = myType
        self.max_size = max_size
        self.v = [None] * max_size
        
        return None

    def begin(self):
        i = 0
        if self.myType == 3:
            while self.v[i] == None:
                i+=1
            return self.v[i].first().item.item

        while self.v[i] == None:
            i+=1
        return self.v[i]

    def end(self):
        i = len(self.v) -1
        if self.myType == 3:
            while self.v[i] == None:
                i-=1
            return self.v[i].last().item.item

        while self.v[i] == None:
            if i == 0: return None
            i-=1
        return self.v[i]

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
        

    def erase(self, toErase):
        key = toErase.key
        d = toErase.myObject

        if self.myType == 3:
            self.v[self.hash(key)].delete(d)
            return True
               
        del self.v[self.hash(key)]
        return True

    def findByHash(self, h):        
        return self.v[h]

    def hash(self, key):
        return (key - 1)

    def findByValue(self, value):
        if self.myType == 3:
            return self.v[self.hash(value)].findByValue(value)

        return self.v[self.hash(value)]

    def print(self):
        if self.myType == 3:
            sum = 0
            for i in self.v:
                if i == None:
                    sum += 1
                    print(str(sum) + ". \t" + str(None))
                else:
                    l = i.getItems()
                    sum += 1
                    print(str(sum) + ". \t")
                    for j in l:
                        print("   -> \t" + str(j.item))
        else:
            sum = 0
            for i in self.v:
                sum+=1
                print(str(sum) + ". \t" + str(i))

