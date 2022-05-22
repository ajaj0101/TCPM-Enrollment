# Create a class that resembles an identity of a person, with their information privy to enrolling on a TCPM form


class Person:
    # Init would hold the person's name in a string
    def setName(self, newName):
        self.name = newName

    # setBirth() will create the person's date of birth in the form of a string
    def setBirth(self, newBirth):
        self.birth = newBirth
    
    # setSex() will create the person's sex in a char or string
    def setSex(self, newSex):
        self.sex = newSex
    
    # setLoc() will define the person's address, city, state, and zip in strings
    def setLoc(self, newAddress, newCity, newState, newZip):
        self.address = newAddress
        self.city = newCity
        self.state = newState
        self.zip = newZip
    
    # setJob() will define the person's occupation in a string
    def setJob(self, newOcc):
        self.occ = newOcc

    # set phone will define the person's work and home phone number in a string 
    def setPhone(self, newHome, newWork):
        self.homePhone = newHome
        self.workPhone = newWork


class EmerContact:
    def setContactName(self, newName):
        self.cName = newName
    
    def setContactPhone(self, newHome, newWork):
        self.home = newHome
        self.work = newWork

class Record:
    def __init__(self, newRecord):
        self.record = newRecord
    
    def setAnswer(self, newAnswer):
        self.answer = newAnswer
    
    def setResponse(self, newResponse):
        self.response = newResponse

gi