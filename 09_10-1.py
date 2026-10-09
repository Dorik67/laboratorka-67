#!/usr/bin/python3
a= list(input())
if len(a) % 2 != 0:
    print('error')
else:
    c=a[::-1]
    if c == a:
        print('yes')
    else:
        print('no')
