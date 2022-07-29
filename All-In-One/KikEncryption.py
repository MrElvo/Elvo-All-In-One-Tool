# ----------Fernet imports----------
import base64
import os
import pathlib
from os import path
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
from Kika import KIKA


  # -----------------------Fernet-----------------------


class Wipe(object):
    def __repr__(self):
        return '\n' * 10000
wipe = Wipe()

def ENCRYPTALL():
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
                            return QUESTIONFERNET()


                        looptimes = input('How many times to run...: ')
                        try:
                            number = int(looptimes)
                            pass
                        except ValueError:
                            print('''
\n-----ERROR-----
Something Isn't right, Numbers only!.
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
                        return ENCRYPTALL()

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
                            return ENCRYPTALL()
                        main()

                    else:
                        print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                        return QUESTIONFERNET()

                elif FERNETQUESTION == '3':
                    from Allinone import ALLINONEMAIN
                    print('\n>>>Back To the Main Menu>>>\n')
                    return ALLINONEMAIN()

                else:
                    return print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n'''), QUESTIONFERNET()

            QUESTIONFERNET()
ENCRYPTALL()
            # -----------------------Fernet-----------------------
