# ----------Banner--------
from pyfiglet import Figlet
from termcolor import colored , cprint
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
- Add colors to each menu


'''
# TODO: -----------TODO-------



custom_fig = Figlet(font='block')
print(colored(custom_fig.renderText("Welcome To Elvo All In One Tool"),'cyan'))


class AllinOne:
    def HackTools(Elvo):
        # custom_menu = Figlet(font='digital')
        print(colored('Welcome to the Main Menu!','magenta',attrs=['reverse', 'blink']))
        print(('''
 | For | Brute-Force >             [1]
 | For | Fernet Encryption >       [2]
 | For | Password Checker+Hasher > [3]
 | For | Wifi Intelligence >       [4]

 '''))
        User_Choice = input("And your choice would be?\n...: ")
        print("You chose...: ", User_Choice)

        # -----------------------Brute Force-----------------------
        if User_Choice == '1':
            def QUESTIONBRUTEFORCE():
                custombruteforce = Figlet(font='bubble')

                print(custombruteforce.renderText('''"Welcome To Elvo\n 
                                                  Brute-Forcer'''))

                BruteIntro = print('''How would you like to Brute Force?

With a Worldlist >         [1]
With Random Numbers >      [2]
With Your Own Characters > [3]
To Main Menu >             [4]
...:''')

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
                            return print(colored('\nsomething is incorrect :( Try again :)\n','red')), QUESTIONBRUTEFORCE()

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
                        return cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold'])),QUESTIONBRUTEFORCE()

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
                        return cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold'])), QUESTIONBRUTEFORCE()

                elif BruteChoice == '4':
                    print(colored('\n>>>Back To the Main Menu>>>','blue'))
                    return object.HackTools('Elvo.a')

                else:
                    print(colored('\nThat\'s not an option.. try again...\n','red'))
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
                iterations=300000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

            def QUESTIONFERNET():

                FERNETQUESTION = input('''What would you like to do?

To Encrypt >   [1]
To Decrypt >   [2]
To Main Menu > [3]
...:''')

                if FERNETQUESTION == '1':
                    # --------------Encryption--------------
                    folderpath = input('Place the Folder Path...: ')
                    looptimes = input('How many times to run...: ')
                    try:
                        number = int(looptimes)
                        pass
                    except ValueError:
                        cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold']))
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

                    #  ------------------DECRYPTION--------------------

                    Question = input("Are you sure? Yes/No...: ").capitalize()
                    if Question == 'Yes':
                        folderpath = input('Place the Folder Path...: ')
                        looptimes = input('How many times to run...: ')
                        try:
                            number = int(looptimes)
                            pass
                        except ValueError:
                            cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold']))
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
                                    print(colored("No more files to decrypt :)",'green'))


                    else:
                        print(colored("That's not one of the options...\n",'yellow'))
                        return QUESTIONFERNET()

                elif FERNETQUESTION == '3':
                    print(colored('\n>>>Back To the Main Menu>>>','blue'))
                    return object.HackTools('Elvo.a')


                else:
                    cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold']))
                    return QUESTIONFERNET()

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
    1. Cant have spaces!.
    2. Has to be in ENGLISH!.
    3. Minimum 6 characters long.
    4. Has to have at least one number.
    5. Has to have at least lower case letter.
    6. Has to have at least one special character.
    7. Has to have at least one upper case character.
                ''')
                PASSWORDQ = input('''Test and Hash OR Main Menu? 
Test and Hash > [1]
Main Menu >     [2]
...:''')
                if PASSWORDQ == '1':
                    PASSWORD = input('Check Your Password...:')
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
                            print(colored("Your Password is strong enough",'red'))
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

                                        print('>>>Back To the Main Menu>>>')
                                        return object.HackTools('Elvo.a')
                                    elif PASSHASH == '2':
                                        break
                                    else:
                                        cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold']))
                                    return PASSHASHER()

                                if y:
                                    print(colored('\n>>>Back To the Main Menu>>>','blue'))
                                    return object.HackTools('Elvo.a')

                            # -------------Password Hasher-------------
                            PASSHASHER()
                            break

                    if x:
                        cprint(colored('''\n
-----ERROR-----
Check the Error above!
Try a different password
-----ERROR-----
\n''','red' , attrs=['bold']))

                        PASSCHECKER()
                elif PASSWORDQ =='2':
                    print(colored('\n>>>Back To the Main Menu>>>','blue'))
                    object.HackTools('Elvo.a')
                else:
                    cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold']))
                    PASSCHECKER()


            PASSCHECKER()

            # -----------------------Password Checker+Hasher-----------------------

            # -----------------------Wifi SSIDs-----------------------
        elif User_Choice == '4':

            customwifissid = Figlet(font='bubble')
            print(customwifissid.renderText("Welcome To Elvo\n "
                                            "Wifi Intelligence"))

            def WIFISSID():
                print('Known Networks OR Available Networks?')
                WIFINETAVA = input('''
Knows Networks >     [1]
Available Networks > [2]
Main Menu >          [3]                
...:''')
                if WIFINETAVA == '1':

                    print('All Known Networks OR Main Menu')
                    WIFIQU = input('''
All Knows Networks >    [1]
Main Menu >             [2] 
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
                                                        WIFINETCON = subprocess.run(["netsh", "wlan", "connect",f"ssid={WIFINAMES[WIFINETWORK]}",f"name={WIFINAMES[WIFINETWORK]}"])
                                                        WIFINETCON
                                                        object.HackTools('Elvo.a')
                                                    except ValueError:
                                                        print('That\'s not one of the Networks... try again..')
                                                        cprint(colored('Choose one of the Networks above. NUMBERS ONLY!','red', attrs=['bold']))
                                                        WIFINET()
                                            WIFINET()

                                        elif WIFICON == '2':
                                            print('\nAs you wish')
                                            object.HackTools('Elvo.a')
                                        else:
                                            cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold']))
                                            WIFICONNECTION()
                                        # -----------------------Wifi Known Network connector-----------------------

                        for x in range(len(WIFILISTNAMES)):
                            print('\n--------------------Wifi Network-----------------------')
                            print(WIFILISTNAMES[x])
                            print(f'---------------------------------------------------------')
                        WIFICONNECTION()

                    # -----------------------Wifi Available Network-----------------------
                    elif WIFIQU == '2':
                        print(colored('\n>>>Back To the Main Menu>>>','blue'))
                        return object.HackTools('Elvo.a')
                    else:
                        cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold']))
                        return WIFISSID()

                elif WIFINETAVA == '2':
                    AVACMD = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True).stdout.decode()
                    print(AVACMD)
                    print(colored('\n>>>Back To the Main Menu>>>','blue'))
                    object.HackTools('Elvo.a')
                elif WIFINETAVA == '3':
                    print(colored('\n>>>Back To the Main Menu>>>','blue'))
                    object.HackTools('Elvo.a')

                else:
                    cprint(colored('\nsomething is incorrect :( Try again :)\n','red', attrs=['bold']))
                    WIFISSID()

                    # -----------------------Wifi Available Network-----------------------

            WIFISSID()
            # -----------------------Wifi SSIDs-----------------------

        else:
            cprint(colored('\n\n\n\nsomething is incorrect :( Try again :)\n','red', attrs=['bold']))
            return object.HackTools('Elvo.a')


object = AllinOne
object.HackTools('Elvo.a')