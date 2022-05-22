# Purpose: To create a command prompt interface that prompts user to input info from keyboard to be stored for an
# applicant to enroll in TCPM

from telnetlib import EC
from Identity import Person

def getPersonal():
    print("Please start with this applicant's personal information:\n")
    name = input("Name: ")
    birthday = input("Birthday: ")
    sex = input("Sex: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zipCode = input("Zip Code: ")
    occ = input("Occupation:" )
    homePhone = input("Home Phone: ")
    workPhone = input("Work Phone: ")
    return [name, birthday, sex, address, city, state, zipCode, occ, homePhone, workPhone]

def getEmerCont():
    print("\n--Enter Emergency Contact--\n")
    e1Name = input("1st Contact's Name: ")
    e1Home = input("1st Contact's Home Phone: ")
    e1Work = input("1st Contact's Work Phone: ")
    return [e1Name, e1Home, e1Work]

def getBackground(record, prompt):
    print(prompt)
    ans = input()
    if ans == 'y':
        resp = input("Explain further:\n")
    else: resp = 'N/A'
    return [record, ans, resp]

def PersonFactory(p,eContact1,eContact2,crimRec,healthRec,medRec,expRec):
    enroll = Person(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8], p[9],
                    eContact1[0],eContact1[1],eContact1[2], eContact2[0], eContact2[1], eContact2[2],
                    crimRec[0],crimRec[1],crimRec[2], healthRec[0], healthRec[1], healthRec[2],
                    medRec[0], medRec[1],medRec[2], expRec[0], expRec[1],expRec[2])
    
    return enroll


# Would you like to enter an applicant
print("Would you like to enter an applicant?")
choice = input("Enter (y/n): ")
while choice == 'y':
    # Phase 1 Gather Info
    personalinfo = getPersonal()
    eContact1 = getEmerCont()
    eContact2 = getEmerCont()
    crimRec = getBackground("Criminal Record", "Do you have any criminal records? (y/n) ")
    healthRec = getBackground("Health", "Do you have any physical or mental conditions which would affect you study in any way? (y/n) ")
    medRec = getBackground("Medication", "Are you on any medication? (y/n) ")
    expRec = getBackground("Experience", "Have you ever trained in any style of Martial Arts before? (y/n) ")

    # Phase 2 Put info into Object
    enroll = PersonFactory(personalinfo, eContact1, eContact2, crimRec, healthRec, medRec, expRec)

    # Phase 3 display and check
    enroll.display()





    







