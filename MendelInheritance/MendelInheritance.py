__author__ = 'Ales'

def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

f = open("sample.txt","r")
dd1,dr1,rr1 = f.readline().split()
dd, dr, rr = int(dd1), int(dr1), int(rr1)
all = dd + dr + rr

print all

proc = 1 - binomialCoeff(rr, 2)/float(all) - rr * dr /float(2*all*all)

print proc