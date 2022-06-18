


# helper functions
# does this information look good?
def get_yes_or_no():
    ans = input("Does this information look correct? (y/n): ")
    validAnswers = ['y','Y','Yes','n','N','No']
    while not ans in validAnswers:
        ans = input ("Invalid answer. Please enter a 'y' for YES or 'n' for NO: ")
    return ans.lower()

# simple yes or no
def get_yes_or_no_2(ans):
    validAnswers = ['y','Y','Yes','n','N','No']
    while not ans in validAnswers:
        ans = input ("Invalid answer. Please enter a 'y' for YES or 'n' for NO: ")
    return ans.lower()


# displays enrollee information
class Enrollee:
    def __init__(self, data):
        self._name = data[0]
        self._bday = data[1]
        self._sex = data[2]
        self._addr = data[3]
        self._homePhone = data[4]
        self._city = data[5]
        self._state = data[6]
        self._zip = data[7]
        self._occ = data[8]
        self._workPhone = data[9]

    def display_Enrollee(self):
        data = [["NAME: "+self._name, "BIRTHDAY: "+self._bday, "SEX: "+self._sex],
                ["ADDRESS: "+self._addr, "HOME PHONE: "+self._homePhone], 
                ["CITY: "+self._city, "STATE: "+self._state, "ZIP: "+self._zip],
                ["OCCUPATION: "+self._occ, "WORK PHONE: "+self._workPhone]]
        col_width = max(len(word) for row in data for word in row) + 8  # padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))
# displays emergency contact information
class EmergencyContact:
    def __init__(self, data):
        self._name = data[0]
        self._homePhone = data[1]
        self._workPhone = data[2]

    def display_Emergency_Contact(self):
        data = [["NAME: "+self._name, "HOME PHONE: "+self._homePhone],
                ["","WORK PHONE: "+self._workPhone]]
        col_width = max(len(word) for row in data for word in row) + 8  # padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))
# displays records information
class Record:
    def __init__(self, data):
        self._ans = data[0]
        self._shortAns = data[1]
    
    def display_Record(self):
        print("Answer: "+self._ans)
        print("Explain: "+self._shortAns)
# displays past experience information
class Experience:
    def __init__(self, data):
        self._ans = data[0]
        self._school = data[1]
        self._style = data[2]
        self._rank = data[3]
    
    def display_Experience(self):
        data = [["Answer: "+self._ans, "School name: "+self._school, "Style: "+self._style],
                ['','',"How long (rank)? "+self._rank]]
        col_width = max(len(word) for row in data for word in row) + 3  # padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))
# gets input for Enrollee, EmergencyContact, Record, and Experience classes to display
class AppInput:

    def get_Enrollee_Input(self):
        # get input
        name = input("NAME: ")
        bday = input("BIRTHDAY: ")
        sex = input("SEX: ")
        addr = input("ADDRESS: ")
        city = input("CITY: ")
        state = input("STATE: ")
        zip = input("ZIP CODE: ")
        occ = input("OCCUPATION: ")
        homePhone = input("HOME PHONE: ")
        workPhone = input("WORK PHONE: ")
        # return input
        return [["NAME: ", "BIRTHDAY: ", "SEX:", "ADDRESS: ", "HOME PHONE: ", "CITY: ", "STATE: ", "ZIP: ", "OCC: ", "WORK PHONE: "],[name, bday, sex, addr, homePhone, city, state, zip, occ, workPhone]]

    def get_Emergency_Contact_Input(self):
        # get input
        name = input("NAME: ")
        homePhone = input("HOME PHONE: ")
        workPhone = input("WORK PHONE: ")
        # return input
        return [["NAME: ", "HOME PHONE: ", "WORK PHONE: "],[name, homePhone, workPhone]]

    def get_Record_Input(self):
        # get input
        ans = input("Answer: ")
        res = get_yes_or_no_2(ans)
        if res == 'y':
            shortAns = input("Explain: ")
        else:
            shortAns = 'N/A'
        # return input
        return [["Answer: ", "Explain: "],[res, shortAns]]

    def get_Experience_Input(self):
        # get input
        ans = input("Answer: ")
        res = get_yes_or_no_2(ans)
        if res == 'y':
            school = input("School name: ")
            style = input("Style: ")
            rank = input("How long (rank)? ")
        else:
            school = 'N/A'
            style = 'N/A'
            rank = 'N/A'
        # return input
        return [['Answer: ', 'School name: ', 'Style: ', 'How long (rank)?'],[res, school, style, rank]]

# gets and checks input
class Application:

    def check_input(self, data, dataLabel, whichClass):
        # display input
        print("-----------------------------------")
        if whichClass == 'Enrollee':
            obj = Enrollee(data)
            obj.display_Enrollee()
        elif whichClass == 'EmergencyContact':
            obj = EmergencyContact(data)
            obj.display_Emergency_Contact()
        elif whichClass == 'Record':
            obj = Record(data)
            obj.display_Record()
        else:
            obj = Experience(data)
            obj.display_Experience()
        print("-----------------------------------")
        # ask if this is correct
        ans = get_yes_or_no()
        while not (ans == 'y' or ans == 'yes'):
            # prompt user for number corresponding 
            print("Please pick the label you want to change with the corresponding number:\n")
            i = 0
            for label in dataLabel:
                print(('('+str(i)+') '+label))
                i = i + 1
            num = input("Number: ")
            # input checking "while num is not between -1 and length of dataLabel:"
            while (int(num) < -1 or int(num) > len(dataLabel)):
                num = input("Invalid answer. Please choose a number from 0 to "+str(len(dataLabel))+": ")   
            # re-type information and re-assign it back to data 
            redo = input(dataLabel[int(num)])
            data[int(num)] = redo
            print("-----------------------------------")
            if whichClass == 'Enrollee':
                obj = Enrollee(data)
                obj.display_Enrollee()
            elif whichClass == 'EmergencyContact':
                obj = EmergencyContact(data)
                obj.display_Emergency_Contact()
            elif whichClass == 'Record':
                obj = Record(data)
                obj.display_Record()
            else:
                obj = Experience(data)
                obj.display_Experience()
            print("-----------------------------------")
            ans = get_yes_or_no()
        return data

    def get_Application_Input(self):
        entry = AppInput()
        enrolleeData = list()
        # get 1 Enrollee input
        print("Please enter Enrollee Information:\n")
        res = entry.get_Enrollee_Input()
        # ask if user input is correct
        dataLabel = res[0]
        data = res[1]
        enrolleeData.append(self.check_input(data, dataLabel,'Enrollee'))

        # get 2 Emergency Contact Inputs
        i = 0
        contactsData = list()
        print("Please enter 2 Emergency Contacts:\n")
        while i < 2:
            res = entry.get_Emergency_Contact_Input()
            # ask if user input is correct
            dataLabel = res[0]
            data = res[1]
            contactsData.append(self.check_input(data, dataLabel, 'EmergencyContact'))
            print("Please enter another contact, if applicable.\n")
            i = i + 1
        # get 3 records
        prompt = ['Do you have any Criminal Records?\n', 'Do you have any Physical/Mental Conditions?\n', 'Are you on any Medication?\n']
        i = 0
        recordsData = list()
        while i < 3:
            print(prompt[i])
            res = entry.get_Record_Input()
            dataLabel = res[0]
            data = res[1]
            recordsData.append(self.check_input(data, dataLabel, 'Record'))
            i = i + 1
        # get n Experiences
        print("Have you ever trained in any style of Martial Arts before? ")
        experienceData = list()
        i = 0
        while i < 2:
            res = entry.get_Experience_Input()
            dataLabel = res[0]
            data = res[1]
            experienceData.append(self.check_input(data, dataLabel, 'Experience'))
            print("Do you have anymore experience?")
            i = i + 1

        return {"Enrollee": enrolleeData, "Emergency Contact": contactsData, "Records": recordsData, "Experience": experienceData}


class DataEntry:
    # get and return all information
    def get_Entry(self):
        obj = Application()
        return obj.get_Application_Input()

    # extract information from dictionary and write to file.
    def extract__write(self, entryData):
        


