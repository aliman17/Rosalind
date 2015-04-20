__author__ = 'Ales'
import re

rex =  re.search("^a*", "aaaabcd")

print rex.group(0)