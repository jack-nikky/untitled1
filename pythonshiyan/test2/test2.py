import time
import turtle
def drawGap():
    turtle.penup()
    turtle.fd(5)

def drawLineRight(draw):
    turtle.right(90)
    drawGap()
    turtle.pendown()  if draw else turtle.penup()
    turtle.fd(40)
    drawGap()


def drawLineLeft(draw):
    turtle.left(90)
    drawGap()
    turtle.pendown()  if draw else turtle.penup()
    turtle.fd(40)
    drawGap()


def drawDigit (digit):
    turtle.goto(0, 0)
    turtle.seth(0)

    drawLineRight(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] \
        else drawLineRight(False)
    drawLineRight(True) if digit in [0, 2, 3, 5, 6, 8, 9] \
        else drawLineRight(False)
    drawLineRight(True) if digit in [0, 2, 6, 8] \
        else drawLineRight(False)
    drawLineRight(True) if digit in [2, 3, 4, 5, 6, 8, 9] \
        else drawLineRight(False)
    drawLineLeft(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] \
        else drawLineLeft(False)
    drawLineLeft(True) if digit in [0,  2, 3, 5, 6, 7, 8, 9] \
        else drawLineLeft(False)
    drawLineLeft(True) if digit in [0, 4, 5, 6, 8, 9] \
        else drawLineLeft(False)
    turtle.penup()
    turtle.fd(20)

turtle.tracer(2)
turtle.setup(400,400)
turtle.pensize(10)
turtle.speed(100)
turtle.pencolor("purple")
turtle.hideturtle()
count = 0
remain = 9
while (remain >= count):
    dida = remain - count
    drawDigit(dida)
    time.sleep(1)
    turtle.clear()
    count += 1
#
# turtle.done()