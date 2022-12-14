import shutil

def WriteInDB(name, phone, filename):
    with open(filename, 'a') as file:
        file.write(name + ';' + phone + ';\n')
        print('All done!')

def ReadFromDBOne(name, filename):
    with open(filename, 'r') as file:
        for n, phone in enumerate(file, 1):
            if name in phone:
                return phone

def ReadFromDBAll(name, filename):
    with open(filename, 'r') as file:
        return list(file)

def ImExToDB(filenameFrom, filenameTo):
    shutil.copyfile(filenameFrom, filenameTo)

def DelFromDB(name, filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            if line.find(name) == -1:
                f.write(line)
           
