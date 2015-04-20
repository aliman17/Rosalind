__author__ = 'Ales'

f = open("sample.txt", 'r')
s = (f.readline()).split(' ')
k, m, n = int(s[0]), int(s[1]), int(s[2])
all = k+m+n

suma = k*(k-1)/float(2) + k*(all-k) + m * (m-1) * 3/float(8) + m* n * 1/2

print 2*suma / float(all*all-all)