from collections import Counter

__author__ = 'Ales'

def frequence(seq):
    """funkcija vrne frekvenco pojavitev nukleotidov ["A", "C", "G", "T"]"""
    counts = Counter(seq)
    return [str(counts[key]) for key in ["A", "C", "G", "T"]]


f = open("sample1.txt","r")
sample = f.read()
print " ".join(frequence(sample))
