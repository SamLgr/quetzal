class Order:
    # Constructor
    # userid: ID of user who ordered
    # timestamp: Timestamp of the order
    # chocolateid: Chocolate milk ID of the order
    # collected: Bool indicating if order was collected
    # currworker: Worker handling the order
    def __init__(self, userid, timestamp, chocolateid, collected):
        self.userid = int(userid)
        self.timestamp = int(timestamp)
        self.chocolateid = int(chocolateid)
        self.collected = collected
        self.currworker= None

    # Destructor
    def __del__(self):
        self.userid = None
        self.timestamp = None
        self.chocolateid = None
        self.collected = None

    # Returns ID of user who ordered
    def getUserid(self):
        return self.userid

    # Returns timestamp of the order
    def getTimestamp(self):
        return self.timestamp

    # Returns chocolate milk ID of the order
    def getChocolateid(self):
        return self.chocolateid

    # Returns if order was collected
    def getCollected(self):
        return self.collected

    # Sets if order was collected to given bool
    def setCollected(self, collected):
        self.collected = collected

    # Returns worker handling the order
    def getWorker(self):
        return self.currworker

    # Sets worker handling the order to given worker
    def setWorker(self, currworker):
        self.currworker = currworker