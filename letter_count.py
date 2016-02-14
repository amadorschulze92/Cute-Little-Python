from collections import Counter
import subprocess
import csv

word = raw_input("text: ")
count = Counter(word)

def alphabet(count):
	for x in 'abcdefghijklmnopqrstuvwxyz':
		print "%s : %d" % (x, count[x]) 

alphabet(count)