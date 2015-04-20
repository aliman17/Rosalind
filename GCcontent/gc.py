from collections import Counter
from sympy.interactive.tests.test_ipython import readline

__author__ = 'Ales'

f = open("sample.txt","r")
sample = f.read()

def frequence(seq):
    """funkcija vrne frekvenco pojavitev nukleotidov ["A", "C", "G", "T"]"""
    counts = Counter(seq)
    return [counts[key] for key in ["A", "C", "G", "T"]]


def gc(sample):
    list = sample.split('>')
    #print list
    best = ["name", 0]
    for case in list[1:]:
        name = case[0:13]
        # print name
        gc = case[14:-1]
        # print gc
        fr = frequence(gc)
        div = float(fr[1]+fr[2])/ (fr[0]+fr[1]+fr[2]+fr[3])
        # print div
        if div > best[1]:
            best[0] = name
            best[1] = div
    print best[0]
    print best[1]

gc (sample)