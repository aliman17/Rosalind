__author__ = 'Ales'


def reverse_complement(record):
    """funkcija vrne komplement in obrat podanega gena"""
    dict = {"A":"T", "C":"G", "T":"A", "G":"C"}
    return "".join([dict[i] for i in str(record) if i != '\n'][::-1])


f = open("sample.txt","r")
sample = f.read()
reverse = reverse_complement(sample)

#print reverse == "ACCGGGTTTT"
print reverse