#!/usr/bin/python3
import turtle
from math import sin
turtle.speed(1)
m=3
R=50
def f(n):
    for i in range(n):
        turtle.left(360/n)
        turtle.forward(2*R*abs(sin(180/n)))
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
n=3
for i in range(m):
    f(n)
    n+=1
    R+=5



