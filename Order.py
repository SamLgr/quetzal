class Order:
    def __init__(self, userid, timestamp, chocolateid, collected):
        self.userid = userid
        self.timestamp = timestamp
        self.chocolateid = chocolateid
        self.collected = collected
        self.currworker= None

    def __del__(self):
        self.userid = None
        self.timestamp = None
        self.chocolateid = None
        self.collected = None

    def getUserid(self):
        return self.userid

    def getTimestamp(self):
        return self.timestamp

    def getChocolateid(self):
        return self.chocolateid

    def getCollected(self):
        return self.collected

    def setCollected(self, collected):
        self.collected = collected