# # Test Evn
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








    









