#!/usr/bin/env python
from operator import itemgetter
import sys

info = dict()
for line in sys.stdin:
	line = line.strip()
	filename, word, index = line.split('\t')
	try:
		a = [int(index)]
	except ValueError:
		continue
    
	if info.has_key(word):
		if info[word].has_key(filename):
			info[word][filename] += a
		else:
			info[word][filename] = a
	else:
		info[word] = {filename : a}            

for key in info.keys():
	print('%s\t%s') % (key, info[key])
