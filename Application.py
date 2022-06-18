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
        print("-----------------------------------------------------------")
        col_width = max(len(word) for row in data for word in row) + 8  # padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))
        print("-----------------------------------------------------------")


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
        print("-----------------------------------------------------------")



obj = Enrollee('Andrew Chiang', '1/11/2001', 'M','3 Fords Run',
    '7818129168','Stoughton','MA','02072','Intern','7818129168')
obj.display_Enrollee()
obj = EmergencyContact('Tracey Chiang', '7813416897','7819298481')
print("IN CASE OF AN EMERGENCY, PLEASE CONTACT:")
obj.display_Emergency_Contact()
