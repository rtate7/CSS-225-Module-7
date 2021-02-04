# Bob Tate
# 2/4/21

# Problem 5: Uses a function call to produce cocentric squares
# in Turtle graphics

import turtle

def drawSquare(t, sz):
    """"Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
scale = 10

for i in range(5):
    drawSquare(alex, (i + 1) * scale * 2)
    alex.up()
    alex.left(180)
    alex.forward(scale)
    alex.left(90)
    alex.forward(scale)
    alex.left(90)
    alex.down()

wn.exitonclick()
