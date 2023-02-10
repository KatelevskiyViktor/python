import view as v

try:
    v.ReadOrWriteNotes()
except:
    print('You entered something wrong, please try again.')
    v.ReadOrWriteNotes()