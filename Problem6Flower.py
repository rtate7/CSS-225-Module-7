# Bob Tate
# 2/4/21

# Problem 6: Uses a function call to produce a flower
# shape in Turtle Graphics

import turtle

def drawHex(t, sz):
    """"Get turtle t to draw a hexagon of sz side"""
    for i in range(6):
        t.forward(sz)
        t.left(60)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("pink")
scale = 50
alex.pensize(2)

for i in range(10):
    drawHex(alex, scale)
    alex.left(36)

wn.exitonclick()