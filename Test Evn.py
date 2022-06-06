# class AllinOne:
#     def HackTools(Elvo):
#
#         print("Welcome to All-in-One-Elvo Tool")
#         print('''
# Choose Your Option From The List Below :)
#
#     1.For Brute-Force enter Brute Force
#     2.For AES encryption enter AES
#  ''')
#         User_Choice = input("And your choice would be?\n...: ").upper()
#         print("You chose...: " , User_Choice.capitalize())
#
#
#         # Test module!
#         # if User_Choice == 'BRUTE FORCE':
#         #     print("Nice")
#         # elif User_Choice == 'AES':
#         #     print("Nice")
#         # else:
#         #     print("Not an option :(")
#
#         # -----------------------Brute Force-----------------------
#         if User_Choice == 'BRUTE FORCE':
#             import requests
#             import random
#
#             BruteIntro = print('''How would you like to Brute Force?
#
#     1.With a Worldlist [1]
#     2.With Random Numbers[2]
#     3.With Your Own Characters[3]
# ''')
#             BruteChoice = input(str("And your choice would be?\n...: "))
#             print("You chose...: ", BruteChoice)
#
#             if BruteChoice == "1":
#                 import requests
#
#                 url = input('Place the URL: ')
#                 username = input('Place the username: ')
#
#                 # chars =  "123"
#
#                 def send_request(username, passwd):
#                     data = {
#                         "username": username,
#                         "password": passwd
#                     }
#
#                     r = requests.get(url, data=data)
#                     return r
#
#                 def implist():
#                     print('ADD .txt TO THE FILE!')
#                     worldlist = input('Wordlist Path...: ')
#                     file = open(worldlist, 'r')
#                     tries = file.read().split('\n')
#                     file.close()
#                     return tries
#
#                 def main(tries):
#                     for passwd in tries:
#                         r = send_request(username, passwd)
#
#                         if 'failed to login' in r.text.lower():
#                             print(f"Incorrect {passwd}\n")
#                         else:
#                             print(f"Correct Password | {passwd} | !\n")
#                             break
#
#                 tries = implist()
#                 main(tries)
#
#             elif BruteChoice == "2":
#
#                 import requests
#                 import random
#
#                 url = input('Place the URL: ')
#                 username = input('Place the username: ')
#                 chars = "abcdefghijklmnopqrstuvwxyz0123456789"
#
#                 def send_request(username, passwd):
#                     data = {
#                         "username": username,
#                         "password": passwd
#                     }
#
#                     r = requests.get(url, data=data)
#                     return r
#
#                 def main():
#                     while True:
#                         rndpasswd = random.choices(chars, k=2)
#                         # k= is the password length.
#                         passwd = "".join(rndpasswd)
#                         # This is how to convert a list to a string. - if we don't convert it to a string if it would print us a list.
#                         r = send_request(username, passwd)
#
#                         if 'failed to login' in r.text.lower():
#                             print(f"Incorrect {passwd}\n")
#                         else:
#                             print(f"Correct Password | {passwd} | !\n")
#                             break
#
#                 main()
#
#             elif BruteChoice == "3":
#                 import requests
#                 import random
#
#                 url = input('Place the URL: ')
#                 username = input('Place the username: ')
#                 chars = input('Write the characters to use')
#
#                 def send_request(username, passwd):
#                     data = {
#                         "username": username,
#                         "password": passwd
#                     }
#
#                     r = requests.get(url, data=data)
#                     return r
#
#                 def main():
#                     while True:
#                         rndpasswd = random.choices(chars, k=2)
#                         # k= is the password length.
#                         passwd = "".join(rndpasswd)
#                         # This is how to convert a list to a string. - if we don't convert it to a string if it would print us a list.
#                         r = send_request(username, passwd)
#
#                         if 'failed to login' in r.text.lower():
#                             print(f"Incorrect {passwd}\n")
#                         else:
#                             print(f"Correct Password | {passwd} | !\n")
#                             break
#
#                 main()
#
#             else:
#                 print("That's not one of the options... start again\n")
#                 return object.HackTools(Elvo)
#         # -----------------------Brute Force-----------------------
#
#
#         # -----------------------AES-----------------------
#         elif User_Choice == 'AES':
#             AESQuestion = input("To Encrypt[1]\nTo Decrypt[2]\n...:")
#
#             import hashlib
#             import base64
#             from Crypto.Cipher import AES
#             from Crypto.Util.Padding import pad, unpad
#             import os
#             from Crypto.Random import get_random_bytes
#
#
#             class AESCipher:
#                 def __init__(self, key):
#                     self.key = b'12345678901234561234567890123456'
#                     # self.key = hashlib.md5(key.encode('utf8')).digest() # - creates randon key
#
#                 def encrypt(self, data):
#                     # iv = get_random_bytes(AES.block_size) - creates random iv
#                     iv = b'12345678901234561234567890123456'
#                     self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
#                     return base64.b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'),
#                                                                          AES.block_size)))
#
#                 def decrypt(self, data):
#                     self.key = b'12345678901234561234567890123456'
#                     raw = base64.b64decode(data)
#                     self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
#                     return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)
#
#
#             if AESQuestion == "1":
#
#
#                 # filepath =input('Place the Path to Encrypt...: ')
#                 folderpath = input('Place the Folder Path...: ')
#
#                 for file in os.listdir(folderpath):
#                     fullpath = f'{folderpath}\{file}'
#
#
#                     msg = open(fullpath, 'r').read()
#                     base64encoding = base64.b64encode(str(msg).encode('ascii'))
#                     SHA256encoding = hashlib.sha256(str(msg).encode('UTF-8')).hexdigest()
#                     print(f'Base64...:{base64encoding}\nSHA256...: {SHA256encoding}')
#
#
#                     print('AES...:', AESCipher('').encrypt(msg).decode('utf-8'))
#                     print('next file')
#
#                     with open(fullpath, 'w') as f:
#                         f.write(AESCipher('').encrypt(msg).decode('utf-8'))
#
#                          # Decrypt part
#
#             elif AESQuestion == "2":
#
#                 Question = input("Are you sure? Yes/No...: ").capitalize()
#
#                 if Question == 'Yes':
#                     folderpath = input('Place the Folder Path...: ')
#
#                     for file in os.listdir(folderpath):
#                         fullpath = f'{folderpath}\{file}'
#
#                         msg = open(fullpath, 'r').read()
#
#                         a = ''
#
#                         print('AES...:', AESCipher(a).decrypt(msg).decode('utf-8'))
#                         print('next file')
#
#                         with open(fullpath, 'w') as f:
#                             f.read()
#                             f.write(AESCipher('').decrypt(fullpath).decode('utf-8'))
#
#                     print('')
#
#                     # folderpath = input(str(r'Place the Folder Path...: '))
#                     #
#                     # for file in os.listdir(folderpath):
#                     #     fullpath = f'{folderpath},{file}'
#                     #
#                     #     # print('Place the file Path to Decrypt')
#                     #     # filepath = input('Place the Path to Decrypt...: ')
#                     #     # print('Place The AES Hash to Decrypt')
#                     #     # decryptmsg = input('AES Hash...: ')
#                     #     # print('Decrypted Has...:\n', AESCipher('').decrypt(decryptmsg).decode('utf-8'))
#
#                         # with open(fullpath, 'w') as f:
#                         #     f.read()
#                         #     f.write(AESCipher('').decrypt(fullpath).decode('utf-8'))
#
#
#                 elif Question == 'No':
#                     print('As you wish')
#
#             else:
#                 print("That's not one of the options... start again\n")
#                 return object.HackTools(Elvo)
#
#
#         # -----------------------AES-----------------------
#         else:
#             print("\nNot an option :( , Try again...\n")
#             return object.HackTools(Elvo)
#
#
# object = AllinOne
# object.HackTools('12345678901234561234567890123456')


#-------------------------------------------------------

#We found the following SHA256 hash: 3752b8cc4f4fa147ce2fdd33689743c2a835900f41b5cfc33ec4cbcab6b33cb5 .
# Plus, we got a breach of passwords db files.
# We need to find out which password this hash belongs to.
# We know the hashing algorithm works like this:
#
# Each password is concatenated with the db file name, and then the hashing algorithm hashes the concatenated string.
#
# For example, a password KASJDNKJNSD that is stored at pass_db1 will generate the hash using: SHA256 on KASJDNKJNSDpass_db1.
# Our goal is to find the password that correlates to the above hash. NOTE: Write it here without the prefix and db file name i.e KASJDNKJNSD
# לקחת את השם של הקובץ ואת התוכן שלו ולהתאים אותם להאש שמוצג למעלה
#
#--------------------Q1---------------------
import os
import hashlib

final_key = "3752b8cc4f4fa147ce2fdd33689743c2a835900f41b5cfc33ec4cbcab6b33cb5"

os.chdir('H:\PythonPro\Test Env\EXAM\Q1') # Data-base path

for file in os.listdir():# open each file in os.listdir

    content = open(file, "r").read() # read the file
    content = content.split("\n")

    for line in content: #inside the file
        a = line+file # shows every line in the file
        b = hashlib.sha256(a.encode("UTF-8")).hexdigest() # encode the lines to sha256

        if final_key in b: # if you fine the final_key in the encrypted hash
            print(line) #print only the line in the file



#-----------------------------Q2------------------------------

# After a while, using the same methodologies we found another breach and the hash: a7312e17ba07ab09dacfebc4cdc2fe516043c1c2fd71078abcebb1e2a017f6c8 .
# But they changed the way they process hashes.
#
# Now each password in the db files contains a prefix with the number of times the password goes through hashing.
#
# For example, for a password stored at pass_db3 that is written in the file like this: 15_SAKDJNKJNASD - the hashing algorithm hashes the
# (first hashing, like previously), then hashes the result's hexdigets (2nd hashing),
# then the result's hexdigets (3rd hashing), until the 15th hashing.

# To verify you understand the algorithm you can use 4_examplePassword assuming it is stored in a file named examplepassdb.
# It should omit this hash: 997a9988839eb94c95a20cee462d956f8d5415c16717cf487ae1066f885a28a1


final_key = "a7312e17ba07ab09dacfebc4cdc2fe516043c1c2fd71078abcebb1e2a017f6c8"

os.chdir('H:\PythonPro\Test Env\EXAM\Q2') # Data-base path

for file in os.listdir():# open each file in os.listdir

    content = open(file, "r").read() # read the file
    content = content.split("\n")
    try:
        for line in content: #inside the file

            line = line.split("_") # מפריד את המספרים ואת ה STR
            looptimes = int(line[0]) # מספר הפעמים שזה חוזר על עצמו

            a = line[1]+file # shows every line in the file
            b = hashlib.sha256(a.encode("UTF-8")).hexdigest() # מצפין כל שורה בFILE

            for counter in range(looptimes): # creates the loop
                b = hashlib.sha256(b.encode("UTF-8")).hexdigest() # hash b in looptimes

                if final_key in b:
                    print(file, line[1], a, b, counter, looptimes) # prints the key that was found
                # print(file, line[1], a, b, counter, looptimes) #print only the line in the file
    except:
        pass


