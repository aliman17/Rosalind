import math

__author__ = 'Ales'

f = open("sample1.txt", 'r')
f.readline()    # throw away name

ch = f.read(1)
string = ""
a = 0
c = 0
while ch != "":
    if ch != '\n':
        string += ch
        if ch == 'A':
            a += 1
        elif ch == 'C':
            c += 1
    ch = f.read(1)

#print string
print a, c
print math.factorial(a) * math.factorial(c)
