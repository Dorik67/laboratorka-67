#!/usr/bin/python3
from turtle import*
from math import*
a = 0
for i in range(6):
    for j in range(360):
        forward(1+a)
        left(1+a)
        a+=0.1
