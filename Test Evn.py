# import os.path
#
# def checkExistence():
#     if os.path.exists("info.txt"):
#         pass
#     else:
#         file = open("info.txt", 'w')
#         file.close()
#
# def appendNew():
#     # This function will append new password in the txt file
#     file = open("info.txt", 'a',encoding='utf-8')
#
#     print()
#     print()
#
#     userName = input("Please enter the user name: ")
#     password = input("Please enter the password here: ")
#     website = input("Please enter the website address here: ")
#     print()
#     print()
#
#     usrnm = str(f"UserName: {userName}  \n")
#     pwd = str(f"Password: {password}  \n")
#     web = str(f"Website: {website}  \n")
#
#     file.write("---------------------------------\n")
#     file.write(usrnm)
#     file.write(pwd)
#     file.write(web)
#     file.write("---------------------------------\n")
#     file.write("\n")
#     file.close
# appendNew()
#
# def readPasswords():
#     file = open('info.txt', 'r')
#     content = file.read()
#     file.close()
#     print(content)
# readPasswords()

# elif WIFINETAVA == '3':
# import subprocess
#
# WIFINAMEMAN = input('Network Name...: ')
# WIFIPASSMAN = input('Network Pass...: ')
#
# CMD = subprocess.run(
#     ["netsh", "wlan", "set", "hostednetwork", "mode=allow", f"ssid={WIFINAMEMAN}",
#      f"key={WIFIPASSMAN}"], capture_output=True).stdout.decode()
# CONNECTCMD = subprocess.run(
#     ["netsh", "wlan", "connect", f"ssid={WIFINAMEMAN}",
#      f"name={WIFINAMEMAN}"])
# CMD
# CONNECTCMD
# print('Connecting... \n')


from Kika import KIKA
class Wipe(object):
    def __repr__(self):
        return '\n' * 10000
wipe = Wipe()


