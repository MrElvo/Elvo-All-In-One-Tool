import re
import subprocess

class Wipe(object):
    def __repr__(self):
        return '\n' * 10000
wipe = Wipe()

def ALLWIFI():
    # customwifissid = Figlet(font='bubble')
    # print(customwifissid.renderText("Welcome To Elvo\n "
    #                                   "Wifi Info"))
    print(wipe)
    print('Welcome To Wifi Intelligence')

    def WIFISSID():
        WIFINETAVA = input('''
Known Networks OR Available Networks OR Main Menu?
Known Networks >     [1]
Available Networks > [2]
Main Menu >          [3]                
...:''')
        if WIFINETAVA == '1':
            print(wipe)

            print(
'All Known Networks OR Connect OR Main Menu')
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
                                                return ALLINONEMAIN()
                                            except ValueError:
                                                print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                                                WIFINET()

                                    WIFINET()


                                elif WIFICON == '2':
                                    from Allinone import ALLINONEMAIN
                                    print(wipe)
                                    print('\nAs you wish')
                                    return ALLINONEMAIN()
                                else:
                                    print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                                    return WIFICONNECTION()
                                # -----------------------Wifi Known Network connector-----------------------

                for x in range(len(WIFILISTNAMES)):
                    print('\n--------------------Wifi Network-----------------------')
                    print(WIFILISTNAMES[x])
                    print(f'---------------------------------------------------------')
                return WIFICONNECTION()

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
                            try:
                                WIFINETCON = subprocess.run(
                                    ["netsh", "wlan", "connect", f"ssid={WIFINAMES[WIFINETWORK]}",
                                     f"name={WIFINAMES[WIFINETWORK]}"])
                                print('\n\n')
                                WIFINETCON
                            except IndexError:
                                print(wipe)
                                print('\n-----KNOWN NETWORKS-----')
                                for i in enumerate(WIFINAMES[:]):
                                    print(*i)
                                    for n in range(0):
                                        print(n)
                                print('\n-----KNOWN NETWORKS-----')

                                print('''
\n-----ERROR-----
Something Isn't right, That's not an option.
-----ERROR-----\n''')
                                WIFINET()

                            return ALLWIFI()
                        except ValueError:
                            print(wipe)
                            print('''
\n-----ERROR-----
Something Isn't right, Numbers only.
-----ERROR-----\n''')
                            print('\n-----KNOWN NETWORKS-----')
                            for i in enumerate(WIFINAMES[:]):
                                print(*i)
                                for n in range(0):
                                    print(n)
                            print('\n-----KNOWN NETWORKS-----')

                            WIFINET()

                WIFINET()


            elif WIFIQU == '3':
                from Allinone import ALLINONEMAIN
                print(wipe)
                print(
'\n>>>Back To the Main Menu>>>\n')
                return ALLINONEMAIN()

            else:
                print(wipe)
                print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
                return WIFISSID()

        elif WIFINETAVA == '2':
            from Allinone import ALLINONEMAIN
            print(wipe)
            AVACMD = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True).stdout.decode()
            print(AVACMD)
            print(
'\n>>>Back To the Main Menu>>>\n')
            return ALLINONEMAIN()



        elif WIFINETAVA == '3':
            from Allinone import ALLINONEMAIN
            print(wipe)
            print(
'\n>>>Back To the Main Menu>>>\n')
            return  ALLINONEMAIN()

        else:
            print(wipe)
            print('''
\n-----ERROR-----
Something Isn't right
-----ERROR-----\n''')
            WIFISSID()

            # -----------------------Wifi Available Network-----------------------

    WIFISSID()
    # -----------------------Wifi SSIDs-----------------------

ALLWIFI()