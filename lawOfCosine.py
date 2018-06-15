import math
from turtle import *


##Law of Cosine

def triangle():

    side1 = int(input("WHAT IS ONE OF THE SIDES OF YOUR TRIANGLE?"))
    side2 = int(input("WHAT IS ANOTHER SIDE OF YOUR TRIANGLE"))
    angle1 = int(input("WHAT IS ONE OF THE ANGLE OF ONE OF YOUR TRIANGLE?"))

    side3 = (pow(side1,2) + pow(side2,2) - ((2)*(side1)*(side2)*(math.cos(math.radians(angle1)))))
    squaredSide3 = pow(side3,0.5)


    angle2First = math.acos(((pow(side2,2)) - (pow(side1,2)) - (pow(squaredSide3,2))) / ((-2 * (side1) * (squaredSide3))))
    angle2Second = math.degrees(angle2First)

    triangleAngle = 180

    angle3 = ((triangleAngle - angle1) - angle2Second)
                        
    ##TURTLE DRAWING
    turt = Turtle()
    turt.goto(0,0)
    turt.down()
    turt.forward(side1)
    turt.left(180 - angle3)
    turt.forward(side2)
    turt.left(180 - angle1)
    turt.forward(squaredSide3)

    print("First Angle: ")
    print(angle1)

    print("Second Angle: ")
    print(angle2Second)

    print("Third Angle: ")
    print(angle3)

if __name__ == "__main__":
        triangle()
