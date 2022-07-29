# -----------Check+Hasher imports-------

import os
import pathlib
import re
import bcrypt
from os import path
from getpass import getpass
from bcrypt import hashpw, gensalt, checkpw

class Wipe(object):
    def __repr__(self):
        return '\n' * 10000
wipe = Wipe()

def ALLPASSCHECKER():
    print('Welcome To Elvo Password Checker and Hasher')

    def PASSCHECKER():
        print(''' 
Here you can check if your password is strong enough
and if it is strong enough,
you can also hash it.
''')

        PASSWORDQ = input('''Test and Hash OR Main Menu? 
Test and Hash >  [1]
Hash A File >    [2]
Main Menu >      [3]
...:''')
        if PASSWORDQ == '1':
            print(wipe)
            print('''
Password MUST have:
1. Cant have spaces!.
2. Has to be in ENGLISH!.
3. Minimum 6 characters long.
4. Has to have at least one number.
5. Has to have at least lower case letter.
6. Has to have at least one special character.
7. Has to have at least one upper case character.
            ''')
            PASSWORD = input('Check Your Password...:')

            x = True
            while x:
                if (len(PASSWORD) < 6 or len(PASSWORD) > 100):
                    print(wipe)
                    print("\nPassword length between 6 and 100 please")
                    break

                elif not re.search("[a-z]", PASSWORD):
                    print(wipe)
                    print("\nYou need at least one lower case letter")
                    break

                elif not re.search("[0123456789]", PASSWORD):
                    print(wipe)
                    print("\nYou need at least one number")
                    break

                elif not re.search("[A-Z]", PASSWORD):
                    print(wipe)
                    print("\nYou need at least one upper case character")
                    break

                elif not re.search("[!@#$%]", PASSWORD):
                    print(wipe)
                    print("\nYou need at least one special character please")
                    break

                elif re.search("\s", PASSWORD):
                    print(wipe)
                    print("\nYou cannot have blank spaces in your password...")
                    break
                else:
                    print("Your Password is strong enough")
                    x = False

                    # -------------Password Hasher-------------
                    def PASSHASHER():
                        print('Hash your Password OR Main Menu')
                        PASSHASH = input('''
Hash My Password >    [1]
Main Menu  >          [2]
...: ''')
                        y = True
                        while y:
                            if PASSHASH == '1':
                                print(wipe)
                                y = False
                                PWDHASH = PASSHASH
                                bytePWDHASH = PWDHASH.encode('utf-8')

                                SALT = bcrypt.gensalt()
                                hash = bcrypt.hashpw(bytePWDHASH, SALT).decode('utf-8')

                                with open('Passwordhash.txt', 'w') as f:
                                    f.write('The Password you hashed: ')
                                    f.write(PASSWORD)
                                    f.write('\nYour Password Hash: ')
                                    f.write(hash)

                                print(wipe)
                                print('Password Info - ')
                                print('Your Password: ', PASSWORD)
                                print('Your Hashed Password:', hash)
                                print('Your Passwords are save in:', os.getcwd() + '\Passwordhash.txt')

                                print('\n>>>Back To the Main Menu>>>\n')

                                from Allinone import ALLINONEMAIN
                                return ALLINONEMAIN()
                            elif PASSHASH == '2':
                                break
                            else:
                                print(wipe)
                                print('''
\n-----ERROR-----
Something Isn't right 
-----ERROR-----\n''')
                            return PASSHASHER()

                        if y:
                            from Allinone import ALLINONEMAIN
                            print(wipe)
                            print('\n>>>Back To the Main Menu>>>\n')
                            return ALLINONEMAIN()

                    # -------------Password Hasher-------------
                    PASSHASHER()
                    break
            if x:
                print('''
\n-----ERROR-----
Something Isn't right, Check above.
-----ERROR-----\n''')
                PASSCHECKER()





        elif PASSWORDQ == '2':
            print('''
Welcome to the file hash section.
DON'T FORGET TO GIVE IT A FULL PATH AND ADD .TXT TO THE FILE!
This would OVERWRITE your file and hash each line inside this file.
Don't forget to save the salt for it.
                    ''')
            FILEPATH = input('File To Hash...: ')
            filepath = pathlib.Path(FILEPATH)
            if filepath.exists():
                path = open(FILEPATH, 'r')
                lines = path.readlines()
                SALT = bcrypt.gensalt()

                path = open(FILEPATH, 'w')
                for line in lines:
                    FILETXT = line.encode('utf-8')
                    SALTS = SALT
                    hash = bcrypt.hashpw(FILETXT, SALTS).decode('utf-8')

                    INSIDEFILE = f'The Line Before: {line} > The Line After: {hash}'
                    path.write('\n--------------------------------------------------------\n')
                    path.writelines(INSIDEFILE)
                    path.write('\n--------------------------------------------------------\n')
                    print(INSIDEFILE)
                print(f'''\n
All Done. 
You can find your file in...: {FILEPATH}
Your salt is...: {SALT}
Save your salt somewhere safe so you can verify your passwords.''')
                return ALLPASSCHECKER()
            else:
                print(wipe)
                print('''
\n-----ERROR-----
Something Isn't right, Path does not exists.
-----ERROR-----\n''')
                return PASSCHECKER()


        elif PASSWORDQ == '3':
            from Allinone import ALLINONEMAIN
            print(wipe)
            print(
                '\n>>>Back To the Main Menu>>>\n')
            return ALLINONEMAIN()
        else:
            print(wipe)
            print('''
    \n-----ERROR-----
    Something Isn't right
    -----ERROR-----\n''')
            PASSCHECKER()

    PASSCHECKER()

    # -----------------------Password Checker+Hasher-----------------------


ALLPASSCHECKER()

