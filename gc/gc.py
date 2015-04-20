__author__ = 'Uporabnik'
import re

def find_num_of_occur(substr, mainstr):
    """Returns num of occurance of a substr in mainstr"""
    return len([m.start() for m in re.finditer(substr, mainstr)])

def find_N(nc, seq) :
    count = 0
    for i in seq:
        if i == nc:
            count +=1
    return count

f = open("sample.txt","r")
name, dev = f.readline(), 0
end = False
nameCur = ""
while True:
    content = ""
    while True:
        c = f.readline()
        if c is "":
            end = True
            break
        elif c[0] == '>':
            nameCur = c
            break

        content += c
    #print name
    g = find_N("G", content)
    c = find_N("C", content)
    r= (g+c)/float(len(content)-1)
    if (r>dev):
        name = nameCur
        #print name, "asdfff"
        dev = r
    if (end):
        break

print name[:-1]
print 100*dev

