from random import random
import turtle

DARTS = 1000*1000
hits = 0

turtle.setup(400,400,200,200)
turtle.penup()
turtle.tracer(20)
turtle.pensize(3)
turtle.pencolor("purple")
turtle.hideturtle()
for i in range(1, DARTS+1):
    x,y = random(),random()

    turtle.goto( 150*x,150* y)
    turtle.pendown()

    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1:
        turtle.fd(1)
        turtle.penup()
        hits += 1
    else:
        turtle.pencolor("red")
        turtle.fd(1)
        turtle.penup()
        turtle.pencolor("purple")
turtle.done()
pi = 4 * (hits/DARTS)
print("pi的值是：{}".format(pi))