


# helper functions
def get_yes_or_no():
        ans = input("Does this information look correct? (y/n): ")
        validAnswers = ['y','Y','Yes','n','N','No']
        while not ans in validAnswers:
            ans = input ("Invalid answer. Please enter a 'y' for YES or 'n' for NO: ")
        return ans



class Enrollee:
    def __init__(self, name, bday, sex, addr, homePhone, city, state, zip, occ, workPhone):
        self._name = name
        self._bday = bday
        self._sex = sex
        self._addr = addr
        self._homePhone = homePhone
        self._city = city
        self._state = state
        self._zip = zip
        self._occ = occ
        self._workPhone = workPhone

    def display_Enrollee(self):
        data = [["NAME: "+self._name, "BIRTHDAY: "+self._bday, "SEX: "+self._sex],
                ["ADDRESS: "+self._addr, "HOME PHONE: "+self._homePhone], 
                ["CITY: "+self._city, "STATE: "+self._state, "ZIP: "+self._zip],
                ["OCCUPATION: "+self._occ, "WORK PHONE: "+self._workPhone]]
        col_width = max(len(word) for row in data for word in row) + 8  # padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))

class EmergencyContact:
    def __init__(self, name, homePhone, workPhone):
        self._name = name
        self._homePhone = homePhone
        self._workPhone = workPhone

    def display_Emergency_Contact(self):
        data = [["NAME: "+self._name, "HOME PHONE: "+self._homePhone],
                ["","WORK PHONE: "+self._workPhone]]
        col_width = max(len(word) for row in data for word in row) + 8  # padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))

class Record:
    def __init__(self, answer, shortAnswer):
        self._ans = answer
        self._shortAns = shortAnswer
    
    def display_Record(self):
        print("Answer: "+self._ans)
        print("Explain: "+self._shortAns)

class Experience:
    def __init__(self, ans, schoolName, style, rank):
        self._ans = ans
        self._school = schoolName
        self._style = style
        self._rank = rank
    
    def display_Experience(self):
        data = [["Answer: "+self._ans, "School name: "+self._school, "Style: "+self._style],
                ['','',"How long (rank)? "+self._rank]]
        col_width = max(len(word) for row in data for word in row) + 3  # padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))

class AppInput:

    def check_enrollee(name, bday, sex, addr, homePhone, city, state, zip, occ, workPhone):
        # display input
        print("-----------------------------------")
        obj = Enrollee(name, bday, sex, addr, homePhone, city, state, zip, occ, workPhone)
        obj.display_Enrollee()
        print("-----------------------------------")


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
        return [name, bday, sex, addr, homePhone, city, state, zip, occ, workPhone]

    def get_Emergency_Contact_Input(self):
        # get input
        name = input("NAME: ")
        homePhone = input("HOME PHONE: ")
        workPhone = input("WORK PHONE: ")
        # return input
        return [name, homePhone, workPhone]

    def get_Record_Input(self):
        # get input
        ans = input("Answer: ")
        shortAns = input("Explain: ")
        # return input
        return [ans, shortAns]

    def get_Experience_Input(self):
        # get input
        ans = input("Answer: ")
        school = input("School name: ")
        style = input("Style: ")
        rank = input("How long (rank)? ")
        # return input
        return [ans, school, style, rank]


        
        '''# display input
        self.check_enrollee(name, bday, sex, addr, homePhone, city, state, zip, occ, workPhone)
        # ask if input is correct
        ans = get_yes_or_no()
        
        ans = ans.lower()
        while not (ans == 'y' or ans == 'yes'):
            dataLabel = ["NAME: ", "BIRTHDAY: ", "SEX:", "ADDRESS: ", "HOME PHONE: ", "CITY: ", "STATE: ", "ZIP: ", "OCC: ", "WORK PHONE: "]
            data = [name, bday, sex, addr, homePhone, city, state, zip, occ, workPhone]
            # prompt user for number corresponding 
            print("Please pick the label you want to change with the corresponding number: (0) Name\n(1) Birthday\n(2) Sex\n(3) Address\n"
                "(4) Home Phone\n(5) City\n(6) State\n(7) Zip\n(8) Occupation\n(9) Work Phone")
            num = input("Number: ")
            # input checking "while num is not between -1 and 10:"
            while not(int(num) > -1 and int(num) < 10):
                num = input("Invalid answer. Please choose a number from 0 to 9: ")
            choice = data[num]    
            redo = input(dataLabel[num]+": ")
            data[num] = redo
            ans = input("Does this information look correct? (y/n): ")'''



obj = AppInput()
obj.get_Enrollee_Input()
obj.get_Emergency_Contact_Input()
obj.get_Record_Input
obj.get_Experience_Input()

