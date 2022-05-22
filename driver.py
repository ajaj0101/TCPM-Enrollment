# Purpose: To create a command prompt interface that prompts user to input info from keyboard to be stored for an
# applicant to enroll in TCPM

from Enroller import Applicant

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
    return [[name],[birthday],[sex],[address],[city],[state],[zipCode],[occ],[homePhone],[workPhone]]

def getEmerCont():
    print("\n--Now Enter 2 Emergency Contacts--\n")
    e1Name = input("1st Contact's Name: ")
    e1Home = input("1st Contact's Home Phone: ")
    e1Work = input("1st Contact's Work Phone: ")
    e2Name = input("2nd Contact's Name: ")
    e2Home = input("2nd Contact's Home Phone: ")
    e2Work = input("2ns Contact's Work Phone: ")
    return [[e1Name],[e1Home],[e1Work],[e2Name],[e2Home],[e2Work]]

def getBackground():
    print("\n--Now Enter Applicant's Background Information--\n")
    crimAns = input("Do you have any criminal records? (y/n): ")
    if crimAns == 'y':
        crimResp = input("Please explain further:\n")
    else: crimResp = 'None'
    healthAns = input("Do you have any physical or mental conditions which would affect your study in any way? (y/n): ")
    if healthAns == 'y':
        healthResp = input("Please explain further:\n")
    else: healthResp = 'None'
    medAns = input("Are you on any medications? (y/n) ")
    if medAns == 'y':
        medResp = input("Please explain further:\n")
    else: medResp = 'None'
    expAns = input("Have you ever trained in any style of Martial Arts before? (y/n) ")
    if expAns == 'y':
        expResp = input("Please explain further:\n")
    else: expResp = 'None'
    return [[crimAns],[crimResp],[healthAns],[healthResp],[medAns],[medResp],[expAns],[expResp]]

# Would you like to enter an applicant
print("Would you like to enter an applicant?")
choice = input("Enter (y/n): ")
while choice == 'y':
    # Create applicant class that has Person, Emergency Contacts, and Backgroud info
    enroll = Applicant()
    # Enter Personal Data
    p = getPersonal()
    # enroll
    enroll.setPerson(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])
    # display
    print("This is what the application looks like so far:\n")
    enroll.displayPersonalInfo()

    # Enter Emergency Contacts
    e = getEmerCont()
    # enroll
    enroll.setEmergencyContacts(e[0], e[1], e[2], e[3], e[4], e[5])
    # display
    print("Please check if emergency contacts are correct:\n")
    enroll.displayContact

    # Enter Background Information
    b = getBackground()
    # enroll
    enroll.setBackground(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7])
    # display
    print("Please check if the background info you entered is correct:\n")
    enroll.displayBackground()

    # store to data base
    # ask to enter another applicant
    choice = input("Would you like to enter another applicant? (y/n)")










