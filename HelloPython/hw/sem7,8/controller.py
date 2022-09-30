import model as m
import re
import logging

def log(name, filename, massage):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info(massage)

def WriteNumber(name, phone, filename):
    log("finction is: WriteNumber", 'log.log', f'Add contact: name-\'{name}\', phone-\'{phone}\', filename-\'{filename}\'')
    m.WriteInDB(name, phone, filename)


def ReadNumber(filename, name = ''):
    if name != '':
        selectedContact = m.ReadFromDBOne(name, filename)
        phone = selectedContact.split(';')
        log("finction is: ReadNumber", 'log.log', f'See contact: name-\'{name}\', phone-\'{phone[1]}\', filename-\'{filename}\'')
        return name + ' phone is: ' + phone[1]
    else:
        log("finction is: ReadNumber", 'log.log', f'See all contacts: filename-\'{filename}\'')
        return m.ReadFromDBAll(name, filename)

def ImportExport(filenameFrom, filenameTo):
    log("finction is: ImportExport", 'log.log', f'Import\export contacts: filename, from-\'{filenameFrom}\', filename, to-\'{filenameTo}\'')
    m.ImExToDB(filenameFrom, filenameTo)
    
def DelContact(name, filename):
    log("finction is: DelContact", 'log.log', f'Delete contact: name-\'{name}\', filename-\'{filename}\'')
    m.DelFromDB(name, filename)