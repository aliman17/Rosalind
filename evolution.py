__author__ = 'Ales'

f = open("sample.txt", 'r')
s = "".join((f.readline()).split('\n'))
t = "".join((f.readline()).split('\n'))

r = 0
for i in range(len(s)):
    if s[i] != t[i]:
        r += 1

print r
