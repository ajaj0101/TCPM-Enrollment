from cmath import exp
import sqlite3
from winreg import ExpandEnvironmentStrings


# helper functions
# does this information look good?
def get_yes_or_no():
    ans = input("Does this information look correct? (y/n): ")
    validAnswers = ['y','Y','Yes','n','N','No']
    while not ans in validAnswers:
        ans = input ("Invalid answer. Please enter a 'y' for no or 'n' for no: ")
    return ans.lower()

# simple yes or no
def get_yes_or_no_2(ans):
    validAnswers = ['y','Y','Yes','n','N','No']
    while not ans in validAnswers:
        ans = input ("Invalid answer. Please enter a 'y' for yes or 'n' for no: ")
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
        # get date
        date = input("Today's Date: ")
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

        return [enrolleeData, contactsData, recordsData, experienceData, date]


class DataEntry:
    # get and return all information
    def get_Entry(self):
        obj = Application()
        return obj.get_Application_Input()

    # extract information from dictionary and write to file.
    def extract__write(self, entryData):
        enrollmentD = entryData[0] # 10 items
        enrollee = enrollmentD[0]

        contactsD = entryData[1] # 6 items
        contact1 = contactsD[0]
        contact2 = contactsD[1]

        recordsD = entryData[2] # 6 items
        r1 = recordsD[0]
        r2 = recordsD[1]
        r3 = recordsD[2]

        experienceD = entryData[3] # 6 items
        exp1 = experienceD[0]


        date = entryData[4]

        # connect db variable to data base
        db = sqlite3.connect('TCPMdb.sqlite')
        # create cursor for db
        cursor = db.cursor()
        cursor.executescript('''

            DROP TABLE IF EXISTS Date;

            CREATE TABLE IF NOT EXISTS Student (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, birthday TEXT,
                sex TEXT, address TEXT, city TEXT, state TEXT, zipcode TEXT, occupation TEXT,
                homephone TEXT, workphone TEXT, contact1 TEXT, contacthome1 TEXT, contactwork1 TEXT,
                contact2 TEXT, contacthome2 TEXT, contactwork2 TEXT, criminal_record_answer TEXT, 
                criminal_record_response TEXT, med_condition_answer TEXT, med_condition_response TEXT,
                medication_answer TEXT, medication_response TEXT, exp_answer TEXT, schoolname TEXT,
                style TEXT, rank TEXT
            );

            CREATE TABLE IF NOT EXISTS Date (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                date TEXT
            );

            CREATE TABLE IF NOT EXISTS Member (
                student_id INTEGER,
                date_id INTEGER,
                PRIMARY KEY (student_id, date_id)
            )
        ''')
        db.commit()

        # enter enrollee information
        cursor.execute('''INSERT OR IGNORE INTO Student (name)
        VALUES ( ? )''', (enrollee[0], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (birthday)
        VALUES ( ? )''', (enrollee[1], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (sex)
        VALUES ( ? )''', (enrollee[2], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (address)
        VALUES ( ? )''', (enrollee[3], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (homephone)
        VALUES ( ? )''', (enrollee[4], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (city)
        VALUES ( ? )''', (enrollee[5], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (state)
        VALUES ( ? )''', (enrollee[6], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (zipcode)
        VALUES ( ? )''', (enrollee[7], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (occupation)
        VALUES ( ? )''', (enrollee[8], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (workphone)
        VALUES ( ? )''', (enrollee[9], ) )
        # enter enrollee emergency contacts
        cursor.execute('''INSERT OR IGNORE INTO Student (contact1)
        VALUES ( ? )''', (contact1[0], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (contacthome1)
        VALUES ( ? )''', (contact1[1], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (contactwork1)
        VALUES ( ? )''', (contact1[2], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (contact2)
        VALUES ( ? )''', (contact2[0], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (contacthome2)
        VALUES ( ? )''', (contact2[1], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (contactwork2)
        VALUES ( ? )''', (contact2[2], ) )
        # enter enrollee records
        cursor.execute('''INSERT OR IGNORE INTO Student (criminal_record_answer)
        VALUES ( ? )''', (r1[0], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (criminal_record_response)
        VALUES ( ? )''', (r1[1], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (med_condition_answer)
        VALUES ( ? )''', (r2[0], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (med_condition_response)
        VALUES ( ? )''', (r2[1], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (medication_answer)
        VALUES ( ? )''', (r3[0], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (medication_response)
        VALUES ( ? )''', (r3[1], ) )
        # enter enrollee exp
        cursor.execute('''INSERT OR IGNORE INTO Student (exp_answer)
        VALUES ( ? )''', (exp1[0], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (schoolname)
        VALUES ( ? )''', (exp1[1], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (style)
        VALUES ( ? )''', (exp1[2], ) )
        cursor.execute('''INSERT OR IGNORE INTO Student (rank)
        VALUES ( ? )''', (exp1[3], ) )
        cursor.execute('''INSERT OR IGNORE INTO Date (date)
        VALUES ( ? )''', (date, ) )

        db.commit()
        
        




        db.close()



obj = DataEntry()
data = obj.get_Entry()
obj.extract__write(data)
