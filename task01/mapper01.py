#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
	line = line.strip()
	words = line.split()
	for word in words:
		pureword = word
#		pureword = re.sub(r'[,.:;?"]','',word)
#		pureword = pureword.replace('[','')
#		pureword = word.replace('[','')
#		pureword = pureword.replace(']','')
#		pureword = pureword.replace('--',' ')
#		pureword - pureword.replace('*'s','')
 		print ("%s\t%s") % (pureword.lower(), 1)
