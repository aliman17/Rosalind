__author__ = 'Ales'


f = open("sample.txt","r")
sample = f.read()
s = ""
for i in sample:
    if i == "T":
        i = "U"
    s += i
print s
#print s == "GAUGGAACUUGACUACGUAAAUU"