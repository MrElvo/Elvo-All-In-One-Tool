# from difflib import Differ
#
# print('''
# Welcome to the File Compartor Section.
# ---Code Meaning---
# ‘-‘ line unique to sequence 1
# ‘+’ line unique to sequence 2
# ‘ 'line common to both sequences
# ‘?’ line not present in either input sequence
# ---Code Meaning---
#
# DON'T FORGET TO ADD .txt TO THE FILE IN ORDER FOR IT TO WORK
# ''')
#
# FILEONE = input('File 1 ...: ')
# FILETWO = input('File 2 ...: ')
#
# with open(FILEONE) as file_1, open(FILETWO) as file_2:
# 	differ = Differ()
#
#
# 	for line in differ.compare(file_1.readlines(), file_2.readlines()):
# 		print(line)
#
#
#
# Python program to test
# internet speed

# import speedtest

# st = speedtest.Speedtest()
# ds = st.download()
# st = speedtest.Speedtest()
# us = st.upload()
# pn = st.results.ping
#
# def humansize(nbytes):
#     suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
#     i = 0
#     while nbytes >= 1024 and i < len(suffixes)-1:
#         nbytes /= 1024.
#         i += 1
#     f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
#     return '%s %s' % (f, suffixes[i])
#
# #Readable
# print('Download Speed:',humansize(ds))
# print('Upload Speed:',humansize(us))
# print('Ping:',pn)

# import urllib.request
# httpsweb = input('For HTTPS...:')
# httpweb = input('For HTTP...:')
# print(urllib.request.urlopen(f"https://www.{httpsweb}.com").getcode())
# print(urllib.request.urlopen(f"http://www.{httpweb}.com").getcode())


import requests

URL = "www.google.com"

try:
    response = requests.head(URL)
except Exception as e:
    print(f"NOT OK: {str(e)}")
else:
    if response.status_code == 200:
        print("OK")
    else:
        print(f"NOT OK: HTTP response code "
              f"{response.status_code}")


