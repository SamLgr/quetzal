class Order:
    def __init__(self, userid, timestamp, chocolateid, collected):
        self.userid = int(userid)
        self.timestamp = int(timestamp)
        self.chocolateid = int(chocolateid)
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