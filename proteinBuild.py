from _license import defaultdict
import collections
__author__ = 'Uporabnik'

dict = {"UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
"UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
"UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
"UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
"UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
"UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
"UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
"UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
"UAU": "Y",      "CAU": "H",      "AAU": "N" ,     "GAU": "D",
"UAC": "Y",      "CAC": "H",      "AAC": "N" ,     "GAC": "D",
"UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA" :"E",
"UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
"UGU": "C",      "CGU": "R",     "AGU": "S" ,     "GGU": "G",
"UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
"UGA": "Stop",   "CGA": "R",      "AGA": "R" ,     "GGA" :"G",
"UGG": "W",      "CGG": "R",      "AGG": "R" ,     "GGG": "G" }

# count number of occurance of each value in dict
counter = defaultdict(int)
for v in dict.values():
    counter[v] += 1

#print counter
f = open("sample.txt", 'r')
sample = "".join((f.read()).split('\n'))

r = 3 # stop codons are included
for i in sample:
    r *= counter[i]

print r % 1000000 # they want to have modulo