#!/usr/bin/python3
from turtle import *
a = 0
for i in range(3):
    for j in range(4):
        forward(100+2*a)
        left(90)
    a+=20
    penup()
    goto(-a,-a)
    pendown()
input()
