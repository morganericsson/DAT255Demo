import sys
from collections import Counter

mytext = open(sys.argv[1]).read()
freq = Counter(mytext.split())

print freq