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
        print("NAME:", self._name, "\t\t\tBIRTHDAY:", self._bday, "\tSEX:", self._sex)
        print("ADDRESS:", self._addr, "\t\t\tHOME PHONE:", self._homePhone)
        print("CITY:", self._city, "\tSTATE:", self._state, "\tZIP CODE:", self._zip)
        print("OCCUPATION:", self._occ, "\t\t\tWORK PHONE:", self._workPhone)


obj = Enrollee('Andrew Chianggggggg', '1/11/2001', 'M','3 Fords Run',
    '7818129168','Stoughton','MA','02072','Intern','7818129168')

obj.displayEnrollee()