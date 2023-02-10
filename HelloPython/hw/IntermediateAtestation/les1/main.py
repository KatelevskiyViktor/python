import view as v

try:
    v.ReadOrWriteNotes()
except:
    print('\n!!!You entered something wrong, please try again!!!\n')
    v.ReadOrWriteNotes()