class User:
    #Constructor
    #param id: The id of this user
    #param firstname: The firstname of this user
    #param lastname: The lastname of this user
    #param mailadress: The mailaddress of this user
    def __init__(self, id, firstname, lastname, mailadress):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.mailadress = mailadress

    #Destructor
    def __del__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.mailadress = None

    #Returns the id of this user
    def getId(self):
        return self.id

    #Returns the name of this user
    def getName(self):
        return self.firstname, self.lastname

    #Returns the mailaddress of this user
    def getMailadress(self):
        return self.mailadress
