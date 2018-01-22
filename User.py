class User:
    # Constructor
    # id: ID to identify the user in ADTs
    # firstname: The first name of the user
    # lastname: The last name of the user
    # mailadress: The e-mail address of the user
    def __init__(self, id, firstname, lastname, mailadress):
        self.id = int(id)
        self.firstname = firstname
        self.lastname = lastname
        self.mailadress = mailadress

    # Destructor
    def __del__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.mailadress = None

    # Returns the ID of the user
    def getId(self):
        return self.id

    # Returns the name of the user as tuple
    def getName(self):
        return self.firstname, self.lastname

    # Returns the e-mail address of the user
    def getMailadress(self):
        return self.mailadress
