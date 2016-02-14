import re
import string

title = raw_input("Job title: ")
var = raw_input("variable: ")

def scramble(title, var):

	titlelist = re.sub("[^\w]", " ",  title).split()
	varlist = re.sub("[^\w]", " ", var).split()
	count = 0

	print "\n-----\n"

	while count <= len(titlelist):
		titlelist.insert(count, var)
		print "or title_freeform ilike '%" + "%".join(titlelist) + "%'"
		count += 1
		titlelist.remove(var)

	print "\n-----"

scramble(title, var)

