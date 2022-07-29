from os import path
from difflib import Differ


class Wipe(object):
    def __repr__(self):
        return '\n' * 10000
wipe = Wipe()

def FILECOMPQ():
    print('''
Welcome to the File Compartor Section.''')
    FILEQ = input('''
Compering Files > [1]
Main Menu >       [2]
...:''')
    if FILEQ == '1':

        print(wipe)

        def FILECOMPARTOR():
            print('''

---Code Meaning---
‘-‘ line unique to sequence 1
‘+’ line unique to sequence 2
‘ 'line common to both sequences
‘?’ line not present in either input sequence
---Code Meaning---

DON'T FORGET TO ADD .txt TO THE FILE IN ORDER FOR IT TO WORK
''')
            FILEONE = input('File 1 ...: ')
            if path.exists(FILEONE):
                FILETWO = input('File 2 ...: ')
                if path.exists(FILETWO):
                    try:
                        with open(FILEONE) as file_1, open(FILETWO) as file_2:
                            differ = Differ()
                    except PermissionError:
                        print(wipe)
                        print('''
That's not a file. Try to enter the FULL file PATH!''')
                        return FILECOMPQ()

                    print(wipe)
                    for line in differ.compare(file_1.readlines(), file_2.readlines()):
                        print(line)

                    def FILECOMPRET():
                        print('''
Back to Main Menu OR another Compare
Another Compare > [1]
Main Menu >       [2]''')
                        FILECOMPBCK = input('...: ')
                        if FILECOMPBCK == '1':
                            return FILECOMPQ()
                        elif FILECOMPBCK == '2':
                            from Allinone import ALLINONEMAIN
                            print(wipe)
                            print(''
'\n>>>Back To the Main Menu>>>\n')
                            return ALLINONEMAIN()
                        else:
                            print(wipe)
                            print('''
\n-----ERROR-----
Something Isn't right, Try again.
-----ERROR-----\n''')
                            return FILECOMPRET()

                    FILECOMPRET()
                else:
                    print(wipe)
                    print('''
\n-----ERROR-----
Something Isn't right, Path does not exists.
-----ERROR-----\n''')
                    return FILECOMPQ()
            else:
                print(wipe)
                print('''
\n-----ERROR-----
Something Isn't right, Path does not exists.
-----ERROR-----\n''')
                return FILECOMPQ()

        FILECOMPARTOR()

    elif FILEQ =='2':
        from Allinone import ALLINONEMAIN
        print(wipe)
        print(''
'\n>>>Back To the Main Menu>>>\n')
        return ALLINONEMAIN()
    else:
        print(wipe)
        print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
        return  FILECOMPQ()
FILECOMPQ()



            # -----------------------File Compartor-----------------------
