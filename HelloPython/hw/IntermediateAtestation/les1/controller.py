import model as m
import logging
import datetime

def log(name, filename, massage):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info(massage)

def WriteNotes(title, msg, dateCreate):
    log("finction is: WriteNumber", 'log.log', f'Add note: title-\'{title}\', msg-\'{msg}\', dateCreate-\'{dateCreate}\'')
    laseNote = m.ReadFromDBLastId()
    cutLastNote = laseNote.split(';')
    m.WriteInDB(int(cutLastNote[0]) + 1, title, msg, dateCreate)

def ReadNotes(title, marker):
    if marker == 'O':
        selectedNote = m.ReadFromDBOne(title)
        note = selectedNote.split(';')
        log("finction is: ReadNotes", 'log.log', f'See note: title-\'{title}\', ID-\'{note[1]}\'')
        return ' ID is: ' + note[0] + ' title is: ' + note[1] + ' message is: ' + note[2] + ' date create is: ' + note[3] + ' date chenges is: ' +  note[4]
    else:
        log("finction is: ReadNotes", 'log.log', f'See all notes or all notes by date')
        return m.ReadFromDBAll()

def EditNoteRead(title):
    log("finction is: EditNoteRead", 'log.log', f'Edit note, reading: note title-\'{title}\'')
    selectedNote = m.ReadFromDBOne(title)
    note = selectedNote.split(';')
    return note

def EditNoteWrite(note):
    log("finction is: EditNote", 'log.log', f'Edit note: title-\'{note[1]}\'')
    ddt = datetime.datetime.today()
    dateChanges = str(ddt.day) + '.' + str(ddt.month) + '.' + str(ddt.year)
    note[4] = dateChanges
    noteCollected = ';'.join(note)
    m.EditFromDB(note[0], noteCollected)

def ImportExport(filenameFrom, filenameTo):
    log("finction is: ImportExport", 'log.log', f'Import\export notes: filename, from-\'{filenameFrom}\', filename, to-\'{filenameTo}\'')
    m.ImExToDB(filenameFrom, filenameTo)
    
def DelNote(title):
    log("finction is: DelNote", 'log.log', f'Delete note: title-\'{title}\'')
    m.DelFromDB(title)