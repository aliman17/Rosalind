from collections import defaultdict

__author__ = 'Ales'
import re

# prefix dictionary where we put under one prefix all strings with
# the same prefix ... this will be useful for searching all strings
# with the same prefix
prefDict = defaultdict(list)
# suffix dictionary with the same meaning as before
sufDict = defaultdict(list)
# list of all input names with corresponding suffices
listOfStrings = []

# open file
f = open("sample1.txt", 'r')

# 1 go through input, and put all of strings into right dicts and into list
f.read(1)   # remove >
while True:
    name = f.read(13)
    if name == "":
        break

    # read context
    c = f.read(1)   # remove \n
    string = ""
    while c != ">" and c != '':
        if c != "\n":
            string += c
        c = f.read(1)
    # if string[-1] == '\n':
    #     string = string[:-1]
    # get prefix, matches with start of string ^
    pattern = string[0:3]
    prefix = re.search(pattern, string).group(0)
    # put into dict
    prefDict[prefix].append(name)
    # get suffix, matches with the end of string $
    pattern = string[-3:]
    suffix = re.search(pattern, string).group(0)
    # put into dict
    sufDict[suffix].append(name)
    listOfStrings.append([name, suffix])
print prefDict
print sufDict
# 2 go through listOfStrings and for each item get matchings and print them out

f = open("result.txt", 'w')
for name, suffix in listOfStrings:
    for other in prefDict[suffix]:
        if name != other:
            #print name, other
            f.write(name+" "+other+"\n")