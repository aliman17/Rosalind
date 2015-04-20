__author__ = 'Uporabnik'


def find_N(nc, seq) :
    count = 0
    for i in seq:
        if i == nc:
            count +=1
    return count

f = open("sample.txt","r")
sample = f.read()
list = sample.split('>')

list = ["".join(i.split("\n")) for i in list[1:]]
best = ["", 0]
for i in list:
    name = i[0:13]
    seq = i[13:]
    c = find_N("C", seq)
    g = find_N("G", seq)
    r = float(g+c)/float(len(seq))
    if r > best[1]:
        best = [name, r]

print best[0]
print best[1]*100