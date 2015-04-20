import re

__author__ = 'Ales'

f = open("sample.txt", 'r')
s = "".join((f.readline()).split('\n'))
t = "".join((f.readline()).split('\n'))

print s
print t

r = [str(m.start()+1) for m in re.finditer('(?='+t+')', s)]
print " ".join(r)