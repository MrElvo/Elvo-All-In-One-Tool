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


PointOne = Point(10,0)
print(PointOne.x)
print(PointOne.y)
PointTwo = Point(5,0)
print(PointTwo.x)
print(PointTwo.y)

print(((PointTwo.x - PointOne.x)**2) + ((PointTwo.y - PointOne.y)**2))**0.5
((3 - 4)**2) + ((0 - 0)**2)**0.5
print()

# √((x_2-x_1)²+(y_2-y_1)²)








    









