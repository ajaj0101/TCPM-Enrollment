# Create a class that resembles an identity of a person, with their information privy to enrolling on a TCPM form


from xml.etree.ElementTree import C14NWriterTarget


class Person:
    # Mutator Methods
    def __init__(self, newName, newBirth, newSex, newAddress, newCity, newState, newZip, newOcc,
                    newHome, newWork, c1N, c1HN, c1WN, c2N, c2HN, c2WN, crimLabel, crimAns, crimResp,
                    healthLabel, healthAns, healthResp, medLabel, medAns, medResp, expLabel, expAns, expResp):
        self.name = newName
        self.birth = newBirth
        self.sex = newSex
        self.address = newAddress
        self.city = newCity
        self.state = newState
        self.zip = newZip
        self.occ = newOcc
        self.pHomePhone = newHome
        self.pWorkPhone = newWork
        self.c1Name = c1N 
        self.c1HomeNum = c1HN
        self.c1WorkNum = c1WN 
        self.c2Name = c2N 
        self.c2HomeNum = c2HN
        self.c2WorkNum = c2WN
        self.crimRec = crimLabel
        self.crimA = crimAns
        self.crimR = crimResp
        self.healthRec = healthLabel
        self.healthA = healthAns
        self.healthR = healthResp
        self.medRec = medLabel
        self.medA = medAns
        self.medR = medResp
        self.expRec = expLabel
        self.expA = expAns
        self.expR = expResp

    def display(self):
        print("--Personal Information--\n")
        print("NAME:", self.name)
        print("BIRTHDAY:", self.birth)
        print("SEX:", self.sex)
        print("ADDRESS:", self.address)
        print("CITY:", self.city)
        print("STATE:", self.state)
        print("ZIP CODE:", self.zip)
        print("OCCUPATION:", self.occ)
        print("HOME PHONE:", self.pHomePhone)
        print("WORK PHONE:", self.pWorkPhone)
        print("\n--Emergency Contacts--\n")
        print("(1)", self.c1Name, "\nHome:", self.c1HomeNum, "\nWork:", self.c1WorkNum)
        print("(2)", self.c2Name, "\nHome:", self.c2HomeNum, "\nWork:", self.c2WorkNum)
        print("\n--Background Information--\n")
        print(self.crimRec, ":", self.crimA, ":", self.crimR)
        print(self.healthRec, ":", self.healthA, ":", self.healthR)
        print(self.medRec, ":", self.medA, ":", self.medR)
        print(self.expRec, ":", self.expA, ":", self.expR)