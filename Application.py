


# helper functions
def get_yes_or_no():
        ans = input("Does this information look correct? (y/n): ")
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
        homePhone = input("HOME PHONE: ")
        city = input("CITY: ")
        state = input("STATE: ")
        zip = input("ZIP CODE: ")
        occ = input("OCCUPATION: ")
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
        shortAns = input("Explain: ")
        # return input
        return [["Answer: ", "Explain: "],[ans, shortAns]]

    def get_Experience_Input(self):
        # get input
        ans = input("Answer: ")
        school = input("School name: ")
        style = input("Style: ")
        rank = input("How long (rank)? ")
        # return input
        return [['Answer: ', 'School name: ', 'Style: ', 'How long (rank)?'],[ans, school, style, rank]]

# gets and checks input
class Application:

    def check_enrollee(self, data, dataLabel):
        # display input
        print("-----------------------------------")
        obj = Enrollee(data)
        obj.display_Enrollee()
        print("-----------------------------------")
        # ask if this is correct
        ans = get_yes_or_no()
        while not (ans == 'y' or ans == 'yes'):
            # prompt user for number corresponding 
            print("Please pick the label you want to change with the corresponding number:\n(0) Name\n(1) Birthday\n(2) Sex\n(3) Address\n"
                "(4) Home Phone\n(5) City\n(6) State\n(7) Zip\n(8) Occupation\n(9) Work Phone")
            num = input("Number: ")
            # input checking "while num is not between -1 and 10:"
            while not(int(num) > -1 and int(num) < 10):
                num = input("Invalid answer. Please choose a number from 0 to 9: ")   
            # re-type information and re-assign it back to data 
            redo = input(dataLabel[int(num)])
            data[int(num)] = redo
            print("-----------------------------------")
            obj = Enrollee(data)
            obj.display_Enrollee()
            print("-----------------------------------")
            ans = get_yes_or_no()
        return data

    def get_Application_Input(self):
        entry = AppInput()

        # get 1 Enrollee input
        res = entry.get_Enrollee_Input()
        # ask if user input is correct
        dataLabel = res[0]
        data = res[1]
        enrolleeData = self.check_enrollee(data, dataLabel)

        # get 2 Emergency Contact Inputs
        res = entry.get_Emergency_Contact_Input()
        # ask if user input is correct
        dataLabel = res[0]
        data = res[1]
        

obj = Application()
obj.get_Application_Input()



