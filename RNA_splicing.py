import Bio.Seq as seq

__author__ = 'Ales'

def read(f):
    ch = f.read(1)
    if ch == '>':
        f.read(13)
    else:
        f.read(12)
    ch = f.read(1)
    seq = ""
    while ch != '>' and ch != '':
        if ch != '\n':
            seq += ch
        ch = f.read(1)
    return seq

f = open("sample2.txt", 'r')
# get DNA sequence
sequence = read(f)
sequenceCopy = sequence
# print sequence
# get all introns
introns = []
intron = read(f)
while intron != '':
    introns.append(intron)
    intron = read(f)
# print introns

for intron in introns:
    sequence = ''.join(sequence.split(intron))

# print sequence
print len(sequence) + sum ([len(i) for i in introns]) == len(sequenceCopy)
print sequence
sequence = seq.translate(sequence)
sequence = sequence[:-1]
print sequence
f = open('result.txt', 'w')
f.write(sequence)