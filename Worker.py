class Worker:
    #Constructor
    #param id: The id of this worker
    #param firstname: The firstname of this worker
    #param lastname: The lastname of this worker
    #param workload: The workload of this worker
    def __init__(self, id, firstname, lastname, workload):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.workload = workload
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
    
    #Sets the status of this worker
    #param status: Status determines if occupied (True/False)
    def setOccupied(self, status):
        self.occupied = status
