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



obj1 = Enrollee('Andrew Chiang', '1/11/2001', 'M','3 Fords Run',
    '7818129168','Stoughton','MA','02072','Intern','7818129168')
obj2 = EmergencyContact('Tracey Chiang', '7813416897','7819298481')
obj3 = EmergencyContact("Hung Chiang", '7813416897','7819561799')
r1 = Record('N', "")
r2 = Record("Y", "ADHD")
r3 = Record("Yes", "Xanax")
exp = Experience('Y','Cobra Kai', 'Cobra','Black Belt')

obj1.display_Enrollee()
print("IN CASE OF AN EMERGENCY, PLEASE CONTACT:")
obj2.display_Emergency_Contact()
obj3.display_Emergency_Contact()
r1.display_Record()
r2.display_Record()
r3.display_Record()
exp.display_Experience()

