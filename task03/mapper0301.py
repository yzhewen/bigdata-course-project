#!/usr/bin/env python

# the first step in task03
from string import punctuation
import sys
import os

fname = os.environ['map_input_file']
for line in sys.stdin:
	line = line.translate(None, punctuation).strip('\t')
	line_contents = line.split(" ")
	doc_name = fname.split('/')[-1]
	for content in line_contents:
		content = content.rstrip()
		key = content + "/" + doc_name
		print('%s\t%s' % (key, 1))
