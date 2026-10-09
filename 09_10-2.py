#!/usr/bin/pytnon3
a=int(input())
l=[]
for i in range(2,10):
    n=a
    while n>0:
        if n%i==0:
            l.append(i)
            n=n//2
print(l)
