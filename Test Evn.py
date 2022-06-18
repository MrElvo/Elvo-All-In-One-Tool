from cryptography.fernet import Fernet, MultiFernet
import os
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
f = MultiFernet([key1, key2])
token = f.encrypt(b"Secret message!")
print(token)

folderpath  = r'D:\Testingfolder'

complete_files = []
for root, dir_names, file_names in os.walk(folderpath):
    for f in file_names:
        complete_files.append(os.path.join(root, f))

        for file in complete_files:
            fullpath = f'{file}'

            msg = open(fullpath, 'r', encoding="utf-8").read()
            token = f.encrypt(msg)
            print(token)
            print(f'\n-----next file-----')

            with open(fullpath, 'w') as f:
                f.write(AESCipher(encrykey).encrypt(msg).decode('UTF-8'))
                f.close()

decryptoken = f.decrypt(token).decode('utf-8')
print(decryptoken)