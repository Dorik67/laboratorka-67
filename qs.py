#!/usr/bin/python3
import turtle
n=10
k=10
turtle.shape('turtle')
def squert(n):
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
for i in range(k):
    squert(n)
    n+=10
    
