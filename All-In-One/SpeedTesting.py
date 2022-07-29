from time import sleep

import speedtest

class Wipe(object):
    def __repr__(self):
        return '\n' * 10000
wipe = Wipe()

print('''
Welcome To The Speed Test Section
Your Speed Test has been started''')
def SPEEDTEST():
    st = speedtest.Speedtest()
    ds = st.download()
    st = speedtest.Speedtest()
    us = st.upload()
    pn = st.results.ping

    def humansize(nbytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while nbytes >= 1024 and i < len(suffixes) - 1:
            nbytes /= 1024.
            i += 1
        f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])

    # Readable
    print(wipe)
    print('''  
  ;~~,__
:-....,-------'`-'._.'
`-,,,  ,       ;'~~'
,'_,'~.__; '--.
//'       ````(;
          ''')
    print('''All Done
Scan Details ''')
    print('Download Speed:', humansize(ds))
    print('Upload Speed:', humansize(us))
    print('Ping:', pn)
    def SPEEDQ():
        sleep(8)
        print(wipe)
        print('''
/^ ^\/
/ 0 0 \/
V\ Y /V
/ - \/
|    \/
|| (__V   
''')
        print('''
Back to Main Menu OR another Speed Test
Speed Test >      [1]
Main Menu >       [2]''')
        SPEEDQINP = input(
'...: ')
        if SPEEDQINP =='1':
            print(wipe)
            print('Another scan has been started ')
            return SPEEDTEST()
        elif SPEEDQINP =='2':
            from Allinone import ALLINONEMAIN
            print(wipe)
            print('\n>>>Back To the Main Menu>>>\n')
            return ALLINONEMAIN()
        else:
            print(wipe)
            print('''
\n-----ERROR-----
Something Isn't right.
-----ERROR-----\n''')
            return SPEEDQ()
    SPEEDQ()
SPEEDTEST()
# -----------------------Speed Test-----------------------

