import shutil

def WriteInDB(id, title, msg, dateCreate):
    with open("db.csv", 'a') as file:
        file.write(str(id) + ";" + title + ';' + msg + ';' + dateCreate + ';' + dateCreate + ';\n')
        print('All done!')

def ReadFromDBOne(title):
        with open("db.csv", 'r') as file:
            for n, note in enumerate(file, 1):
                if title in note:
                    return note

def ReadFromDBLastId():
    with open("db.csv") as f:
        for line in f:
            pass
        return line

def ReadFromDBAll():
    with open("db.csv", 'r') as file:
        return list(file)

def ImExToDB(filenameFrom, filenameTo):
    shutil.copyfile(filenameFrom, filenameTo)

def DelFromDB(title):
    with open("db.csv", "r") as f:
        notes = f.readlines()
    with open("db.csv", "w") as f:
        for note in notes:
            if note.find(title) == -1:
                f.write(note)

def EditFromDB(id, note):
    with open("db.csv", "r") as f:
        notes = f.readlines()
    with open("db.csv", "w") as f:
        for n in notes:
            if n.find(id) == -1:
                f.write(n)
            else:
                f.write(note)
           
