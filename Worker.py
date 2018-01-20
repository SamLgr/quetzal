
"""
>>> worker = Worker(0, "", "", 4)
>>> worker.setId(1)
>>> worker.getId()
1
>>> worker.setFirstname("Foo")
>>> worker.setLastname("Bar")
>>> worker.getName()
('Foo', 'Bar')
>>> worker.setWorkload(8)
>>> worker.getWorkload()
8
>>> worker.setOccupied(True)
>>> worker.getOccupied()
True
>>> worker.setOrder(2)
>>> worker.getOrder()
2
"""
class Worker:
    id = 0
    firstname = ""
    lastname = ""
    workload = 0

    #Constructor
    #param id: The id of this worker
    #param firstname: The firstname of this worker
    #param lastname: The lastname of this worker
    #param workload: The workload of this worker
    def __init__(self, id, firstname, lastname, workload):
        self.id = int(id)
        self.firstname = firstname
        self.lastname = lastname
        self.workload = int(workload)
        self.occupied = False
        self.order = None
    
    #Constructor
    def __del__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.workload = None
        self.occupied = None
        self.order = None

    #Returns the id of this worker
    def getId(self):
        return self.id

    #Returns the name of this worker
    def getName(self):
        return self.firstname, self.lastname
    
    #Returns the workload of this worker
    def getWorkload(self):
        return self.workload

    #Returns if this worker is occupied
    def getOccupied(self):
        return self.occupied
   
    #Returns the order of this worker
    def getOrder(self):
        return self.order

    
    #Sets id of worker
    #:param id: Id to set
    def setId(self, id):
        self.id = id

    #Sets firstname of worker
    #:param firstname: Firstname to set
    def setFirstname(self, firstname):
        self.firstname = firstname

    #Sets lastname of worker
    #:param lastname: Lastname to set
    def setLastname(self, lastname):
        self.lastname = lastname

    #Sets workload of worker
    #:param workload: Workload to set
    def setWorkload(self, workload):
        self.workload = workload

    #Sets if worker is occupied
    #:param occupied: Occupied or not
    def setOccupied(self, occupied):
        self.occupied = occupied

    #Sets order worker is working on
    #:param order: order worker is working on
    def setOrder(self, order):
        self.order = order
