import controller as ctr

def ReadOrWritePhoneNumber():
    while True:
        val = input('Hi!Do you want to write (please enter W), or read(please enter R): ')

        if val == 'W':
            phone = input('Enter number, format is "+79696996969": ')
            name = input('Enter name, format is "Ilya": ')
            filename = input('Enter file name, format is "file.csv": ')
            ctr.writeNumber(name, phone, filename)
        elif val == 'R':
            choise = input('Do you want see all dir(Enter \'A\') or one name number(Enter \'O\'): ')
            if choise == 'O':
                name = input('Enter name, format is "Ilya": ')
                filename = input('Enter file name, format is "file.csv": ')
                print(ctr.readNumber(filename, name))
            else:
                filename = input('Enter file name, format is "file.csv": ')
                print('Your phone number guide is: ')
                for n in ctr.readNumber(filename):
                    print(n)

