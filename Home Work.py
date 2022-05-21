# Home Work


# --- Function Task ---
# a = "CHANGE!"

# def funca():
#     global a
#     print("This is funcA ")
#     myarg = 'TEAM A'
#     a = 'A'
#     print("Change made by A" + a)
#     return print('FuncB return')


# def funcb():
#     global a
#     print("This is FuncB")
#     myarg = 'TEAM B'
#     a = 'B'
#     print("Change made by B " + a)
#     return print('FuncB return')



# funca()
# funcb()

# global a
# a="CHANGE!"

# user_cho=input('A or B - ')

# def funca():
#     print("Change made by A "+ a)
#     # print(a)
# #returnprint('END Func A return')



# def funcb():
#     print("Change made by B "+ a)
#     # print(a)
#     #returnprint('END Func B return')

# if user_cho=='A':
#     funca()
# else:
#     funcb()

# print('DONE!')


#_____________________________________
# global a
# global b
# a='TeamA'
# b='TeamB'
# c=''
# user_ch=input("choosea/b:")

# def functionAB(args,args2):
#     if user_ch=='a':
#         args+=a
#         print(args)
#     else:
#         args2+=b
#         print(args2)

# functionAB(c,c)
# _____________________________________
# args+=a
# args2+=b
# return print("nothing")


# def functionB(b):
#     print('B')
#     b+='TeamB'
#     #returnprint(b)

# functionA(a)
# functionB(b)


# ------------TO DO!--------

# def funca():
#     pass

# def funcb():
#     pass



# msg = "global msg"

# print(msg) - הודעה כללית
# print() - funca - פונקציה A
# print(msg) - changed by funca - השינוי שפונקציה A עשתה לMSG
# print() - funcb - פונקציה B
# print(msg) - changed by funcb - השינוי שפונקציה B עשתה ל MSG


# --------------------

#Objects - תדפיס את המרחק בין ה 2 נקודות.


class Point:
    def __init__(self, argX, argY):
        self.x = argX 
        self.y = argY
        return


    def dst(other_point,arg2X,arg2Y):
        other_point.x = arg2X
        other_point.y = arg2Y
        return 


Themath = Point(3,0)
print(Themath.x)
print(Themath.y)
other_point = Point(4,5)
print(other_point.x)
print(other_point.y)

print(((other_point.x- Themath.x)**2) + ((other_point.y - Themath.y)**2)**0.5)
# print(Themath.dst(other_point))

       # (x1-x2)**2+(y1-y2)**2
        # other_point = ((self.x - self.y) * 2) + ((self.y - self.x) * 2)**0.5
        # self.dsty = ((self.x - self.y) * 2) + ((self.y - self.x) * 2)**0.5




