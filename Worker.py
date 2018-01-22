
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

    # Constructor
    # id: The ID of the worker
    # firstname: The first name of the worker
    # lastname: The last name of the worker
    # workload: The workload of the worker
    # occupied: Bool indicating if the worker is occupied
    # order: Order being handled by the worker
    def __init__(self, id, firstname, lastname, workload):
        self.id = int(id)
        self.firstname = firstname
        self.lastname = lastname
        self.workload = int(workload)
        self.occupied = False
        self.order = None
    
    # Constructor
    def __del__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.workload = None
        self.occupied = None
        self.order = None

    # Returns the ID of the worker
    def getId(self):
        return self.id

    # Returns the name of the worker
    def getName(self):
        return self.firstname, self.lastname
    
    # Returns the workload of the worker
    def getWorkload(self):
        return self.workload

    # Returns if the worker is occupied
    def getOccupied(self):
        return self.occupied
   
    # Returns order being handled by the worker
    def getOrder(self):
        return self.order
    
    # Sets ID of the worker to given ID
    def setId(self, id):
        self.id = id

    # Sets first name of the worker to given first name
    def setFirstname(self, firstname):
        self.firstname = firstname

    # Sets last name of the worker to given last name
    def setLastname(self, lastname):
        self.lastname = lastname

    # Sets workload of the worker to given workload
    def setWorkload(self, workload):
        self.workload = workload

    # Sets if worker is occupied to given bool
    def setOccupied(self, occupied):
        self.occupied = occupied

    # Sets order being handled by the worker to given order
    def setOrder(self, order):
        self.order = order
