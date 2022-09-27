import controller as ctr

def ReadOrWritePhoneNumber():
    while True:
        val = input('Hi!Do you want to write (please enter W), or read(R)\n, or import\export(I): ')

        if val == 'W':
            phone = input('Enter number, format is "+79696996969": ')
            name = input('Enter name, format is "Ilya": ')
            filename = input('Enter file name, format is "file.csv": ')
            ctr.WriteNumber(name, phone, filename)
        elif val == 'R':
            choise = input('Do you want see all contacts(Enter \'A\') or one number(Enter \'O\'): ')
            if choise == 'O':
                name = input('Enter name, format is "Ilya": ')
                filename = input('Enter file name, format is "file.csv": ')
                print(ctr.ReadNumber(filename, name))
            else:
                filename = input('Enter file name, format is "file.csv": ')
                print('Your phone number guide is: ')
                for n in ctr.ReadNumber(filename):
                    print(n)
        elif val == 'I':
            filenameFrom = input('Enter file name, format is "file.csv" from: ')
            filenameTo = input('Enter file name, format is "file.csv": ')
            ctr.ImportExport(filenameFrom, filenameTo)
            print('Copied!')

