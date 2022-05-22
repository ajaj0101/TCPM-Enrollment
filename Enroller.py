# Purpose: to create a program that uses the classes from Identity to create and store information
# that would be on an Enrollment application

from Identity import Person, Record, EmerContact

class Enroller:
    person = Person()
    emergencyContact1 = EmerContact()
    emergencyContact2 = EmerContact()
    criminalRecord = Record("Criminal Record")
    health = Record("Health")
    meds = Record("Medicine")
    experience = Record("Martial Arts Experience")

    def setPerson(self, newName, newBirth, newSex, newAddress, newCity, newState, newZip, newOcc, newHomePhone, newWorkPhone):
        self.person.setName(newName)
        self.person.setBirth(newBirth)
        self.person.setSex(newSex)
        self.person.setLoc(newAddress, newCity, newState, newZip)
        self.person.setJob(newOcc)
        self.person.setPhone(newHomePhone, newWorkPhone)
    
    def setEmergencyContacts(self, cName1, cHomePhone1, cWorkPhon1, cName2, cHomePhone2, cWorkPhone2):
        self.emergencyContact1.setContactName(cName1)
        self.emergencyContact1.setContactPhone(cHomePhone1, cWorkPhon1)
        self.emergencyContact2.setContactName(cName2)
        self.emergencyContact2.setContactPhone(cHomePhone2, cWorkPhone2)

    def setBackground(self, )