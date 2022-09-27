import model as m
import re




def WriteNumber(name, phone, filename):
    m.WriteInDB(name, phone, filename)


def ReadNumber(filename, name = ''):
    if name != '':
        selectedContact = m.ReadFromDBOne(name, filename)
        return name + ' phone is: ' + re.sub(name + ";", '', selectedContact)
    else:
        return m.ReadFromDBAll(name, filename)

def ImportExport(filenameFrom, filenameTo):
    m.ImExToDB(filenameFrom, filenameTo)
    
