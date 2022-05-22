# Purpose: to create a program that uses the classes from Identity to create and store information
# that would be on an Enrollment application

from Identity import Person, Record, EmerContact

class Applicant:
    person = Person()
    emergencyContact1 = EmerContact()
    emergencyContact2 = EmerContact()
    criminalRecord = Record("Criminal Record")
    health = Record("Health")
    meds = Record("Medication")
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

    def setBackground(self, a1, a2, a3, a4, r1, r2, r3, r4):
        self.criminalRecord.setAnswer(a1)
        self.criminalRecord.setResponse(r1)

        self.health.setAnswer(a2)
        self.health.setResponse(r2)

        self.meds.setAnswer(a3)
        self.meds.setResponse(r3)

        self.experience.setAnswer(a4)
        self.experience.setResponse(r4)

    def displayPersonalInfo(self):
        print("NAME:", self.person.name)
        print("BIRTHDAY:", self.person.birth)
        print("SEX:", self.person.sex)
        print("ADDRESS:", self.person.address)
        print("CITY:", self.person.city)
        print("STATE:", self.person.state)
        print("ZIP CODE:", self.person.zip)
        print("OCCUPATION:", self.person.occ)
        print("HOME PHONE:", self.person.homePhone)
        print("WORK PHONE:", self.person.workPhone)

    def displayContact(self):
        print("\n--Contact # 1--\n")
        print("NAME:", self.emergencyContact1.cName)
        print("HOME PHONE:", self.emergencyContact1.home)
        print("WORK PHONE:", self.emergencyContact1.work)
        print("--Contact # 2--\n")
        print("NAME", self.emergencyContact2.cName)
        print("HOME PHONE:", self.emergencyContact2.home)
        print("WORK PHONE:", self.emergencyContact2.work)


    def displayBackground(self):
        print("--", self.criminalRecord.record, "--\n")
        print("Answer:", self.criminalRecord.answer)
        print("Response:", self.criminalRecord.response)
        print("\n--", self.health.record, "--\n")
        print("Answer:", self.health.answer)
        print("Response:", self.health.response)
        print("\n--", self.meds.record, "--\n")
        print("Answer:", self.meds.answer)
        print("Response:", self.meds.response)
        print("\n--", self.experience.record, "--\n")
        print("Answer:", self.experience.answer)
        print("Response:", self.experience.response)  
