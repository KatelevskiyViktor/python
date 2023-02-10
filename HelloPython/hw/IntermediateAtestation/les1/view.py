import controller as ctr

def ReadOrWriteNotes():
    while True:
        val = input('\n\nHi! Select: write note (enter W),\nread(R), \nedit(E),\nimport\export(I),\ndel(D),\nexit(Q): ')

        if val == 'W':
            title = input('Enter title: ')
            msg = input('Enter message: ')
            dateCreate = input('Enter date, format is "dd.mm.yyyy": ')
            ctr.WriteNotes(title, msg, dateCreate)
        elif val == 'R':
            choise = input('Do you want see all notes(Enter \'A\')\nor one note(Enter \'O\')\nor note by date(Enter \'D\'): ')
            if choise == 'O':
                title = input('Enter title note: ')
                print(ctr.ReadNotes(title, choise))
            elif choise == 'D':
                date = input('Enter date note, format is "dd.mm.yy": ')
                print('Your notes by date is: ')
                for note in ctr.ReadNotes('D', 'D'):
                    if date in note:
                        print(note)
            else:
                print('Your notes is: ')
                for n in ctr.ReadNotes('A', 'A'):
                    print(n)
        elif val == 'E':
            title = input('Enter title: ')
            note = ctr.EditNoteRead(title)
            titleNew = input('\nYour old title: ' + note[1] + '\n' + 'Enter new title: ')
            msg = input('\nYour old message: ' + note[2] + '\n' + 'Enter new message: ')
            dateCreate = input('\nYour old date: ' + note[3] + '\n' + 'Enter new date, format is "dd.mm.yy": ')
            note[1] = titleNew
            note[2] = msg
            note[3] = dateCreate
            ctr.EditNoteWrite(note)
            print('\nAll done!\n')
        elif val == 'I':
            filenameFrom = input('Enter db file name from: ')
            filenameTo = input('Enter db file name to: ')
            ctr.ImportExport(filenameFrom, filenameTo)
            print('Copied!')
        elif val == 'D':
            title = input('Enter title: ')
            ctr.DelNote(title)
            print('Note was deleted!')
        else:
            print('Goodbye=****!')
            break

