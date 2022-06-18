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

    def displayEnrollee(self):
        data = [[self._name, self._bday, self._sex],[self._addr, self._homePhone], [self._city, self._state, self._zip],[self._occ, self._workPhone]]
        col_width = max(len(word) for row in data for word in row) + 2  # padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))
        '''print("NAME:", self._name, "\t\t\tBIRTHDAY:", self._bday, "\tSEX:", self._sex)
        print("ADDRESS:", self._addr, "\t\t\tHOME PHONE:", self._homePhone)
        print("CITY:", self._city, "\tSTATE:", self._state, "\tZIP CODE:", self._zip)
        print("OCCUPATION:", self._occ, "\t\t\tWORK PHONE:", self._workPhone)'''


obj = Enrollee('Andrew Chiang', '1/11/2001', 'M','3 Fords Run',
    '7818129168','Stoughton','MA','02072','Intern','7818129168')

obj.displayEnrollee()