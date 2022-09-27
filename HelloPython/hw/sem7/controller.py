import model as m
import re


def writeNumber(name, phone, filename):
    m.WriteInDB(name, phone, filename)


def readNumber(filename, name = ''):
    if name != '':
        selectedContact = m.ReadFromDBOne(name, filename)
        return name + ' phone is: ' + re.sub(name + ";", '', selectedContact)
    else:
        return m.ReadFromDBAll(name, filename)