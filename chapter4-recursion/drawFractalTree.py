import turtle
import random

def tree(branchLen, t, penSize, defaultColor):
    if branchLen > 5:
        t.pensize(penSize)
        t.color(defaultColor)
        t.pendown()

        # Leaves are green
        if branchLen <= 15:
            t.color("green")

        leftAngle = random.randrange(30,40)
        rightAngle = random.randrange(30,40)
        leftBranchLenShorten = random.randrange(10,15)
        rightBranchLenShorten = random.randrange(10,15)
        leftPenSize = 1 if penSize == 1 else penSize - 1
        rightPenSize = 1 if penSize == 1 else penSize - 1

        # Branch trunk
        t.forward(branchLen)

        # Right branch
        t.right(rightAngle)
        tree(branchLen - rightBranchLenShorten, t, rightPenSize, defaultColor)
        t.left(rightAngle)

        # Left branch
        t.left(leftAngle)
        tree(branchLen - leftBranchLenShorten, t, leftPenSize, defaultColor)
        t.right(leftAngle)

        t.color(defaultColor)
        t.penup()
        t.backward(branchLen)

if __name__ == "__main__":
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed("fastest")
    tree(
        branchLen=105,
        penSize=8,
        defaultColor="brown",
        t=t
    )
    myWin.exitonclick()

