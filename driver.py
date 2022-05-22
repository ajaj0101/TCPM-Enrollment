# Purpose: To create a command prompt interface that prompts user to input info from keyboard to be stored for an
# applicant to enroll in TCPM

from Enroller import Applicant



# Would you like to enter an applicant
print("Would you like to enter an applicant?")
choice = input("Enter (y/n): ")
while choice == 'y':
    # Create applicant class that has Person, Emergency Contacts, and Backgroud info
    enroll = Applicant()
    # Enter Personal Data
    print("Please start with this applicant's personal information:\n")
    name = input("Name: ")
    birthday = input("Birthday: ")
    sex = input("Sex: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zipCode = input("Zip Code: ")
    

