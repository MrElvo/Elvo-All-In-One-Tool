# ----------Banner--------
from pyfiglet import Figlet


# from termcolor import colored, cprint

# http://www.figlet.org/examples.html - fonts

# ----------Fernet imports----------

class Wipe(object):
    def __repr__(self):
        return '\n' * 10000


wipe = Wipe()

def ALLINONEMAIN():
    print(wipe)
    print('Welcome to All-In-One Elvo Tool')
    print(('''
    Welcome to the Main Menu!
--------------------------------------
| For | Brute-Force >             [1]
| For | Elvo Encryption >         [2]
| For | Password Checker+Hasher > [3]
| For | Wifi Intelligence >       [4]
| For | File Compartor >          [5]
| For | Speed Test >              [6]
--------------------------------------
     '''))

    User_Choice = input("And your choice would be?\n...: ")
    print(wipe)
    print("You chose...: ", User_Choice)

    if User_Choice == '1':
        from BruteForceAll import QUESTIONBRUTEFORCE
        QUESTIONBRUTEFORCE()
    elif User_Choice == '2':
        from KikEncryption import ENCRYPTALL
        ENCRYPTALL()
    elif User_Choice == '3':
        from PassChecker import ALLPASSCHECKER
        ALLPASSCHECKER()
    elif User_Choice == '4':
        from WifiReco import ALLWIFI
        ALLWIFI()
    elif User_Choice == '5':
        from FileComp import FILECOMPARTOR
        FILECOMPARTOR()
    elif User_Choice == '6':
        from SpeedTesting import SPEEDTEST
        SPEEDTEST()
    else:
        from Kika import KIKA
        KIKA()


ALLINONEMAIN()
