#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t', 1)
	try:
		count = int(count)
	except ValueError: # if count was not a number, ignore/discard that line
		continue
	if current_word == word:
		current_count += count
	else:
		if current_word:
			print ("%s\t%s") % (current_word, current_count)
 		current_count = count
 		current_word = word

if word == current_word: 
	print ("%s\t%s") % (current_word, current_count)
