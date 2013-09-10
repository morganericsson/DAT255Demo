import sys
from collections import Counter
import string

mytext = open(sys.argv[1]).read()
freq = Counter([ w.translate(None, string.punctuation).lower() for w in mytext.split() ])

print freq