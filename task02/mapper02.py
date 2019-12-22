#!/usr/bin/env python

import sys
import re
import os

counter=0
for (nums, lines) in enumerate(sys.stdin):
	counter += 1
	line = lines.strip()
	words = lines.split()
#	for num in nums:
#	filename = os.environ["mapreduce_map_input_file"]
	for word in words:
		pureword = word
		filename = os.environ["mapreduce_map_input_file"]
#		pureword = re.sub(r'[,.:;?"]','',word)
#		pureword = pureword.replace('[','')
#		pureword = pureword.replace(']','')
#		pureword = pureword.replace('--',' ')
#		pureword - pureword.replace('*'s','')
 		print ("%s\t%s\t%s") % (filename.split('/')[-1], pureword.lower(), counter)
