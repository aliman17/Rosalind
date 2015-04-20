from collections import defaultdict

__author__ = 'Ales'

f = open("sample1.txt", 'r')

f.readline()    # da se znebimo imena

#nucls = defaultdict(list)

ch = f.read(1)
string = ""
pos = 0
while ch != "":
    if ch != '\n':
        string += ch
        #nucls[ch].append(pos)
        pos += 1
    ch = f.read(1)
# print string
# print nucls

# general dict of nucls
nucls = {"A":"U", "C":"G", "G":"C", "U":"A"}
# dynamicTable for saving results positions*positions
dynamicTable = [[-1 for i in xrange(len(string))] for i in xrange(len(string))]
#print dynamicTable
def recursive(startPos, stopPos, string):
    o = [startPos, stopPos]
    # check if alreadz computed

    if stopPos - startPos == -1:
        return 1
    elif stopPos - startPos < -1:
        raise Exception("Ni v redu")

    if dynamicTable[startPos][stopPos] != -1:
        return dynamicTable[startPos][stopPos]



    count = {"A":0, "C":0, "G":0, "U":0}
    # edge is list of positions, where we can end our edge which
    # starts at position startPos
    edge = []
    # count a, c, g and u
    # if a = u and g = c, then it's ok, otherwise we'll return 0
    # we know, that first char has to connect to someone else so we can
    # check during this count, if there is somewhere a=u and c = g
    # if it is, we can add an edge - this will reduce number of
    # counting
    # to so, we have to skip startPos, because we don't want to count it among
    # pos is variable for position of ending of the edge - relative position
    for pos in range(startPos, stopPos+1):
        count[string[pos]] += 1
        if count["A"] == count["U"] and count["C"] == count["G"] and string[pos] == nucls[string[startPos]]:
            edge.append(pos)

    #count[string[startPos]] += 1    # repair skipped first character
    if count["A"] != count["U"] and count["C"] != count["G"]:
        return 0
    # add one edge, and then loop over all possibilities
    result = 0

    #print edge
    for pos in edge:
        result += recursive(startPos+1, pos-1, string)*recursive(pos+1, stopPos, string)
        # recursive left


        # recursive right
    dynamicTable[startPos][stopPos] = result
    return result

print recursive(0, len(string)-1, string)%1000000
#print dynamicTable