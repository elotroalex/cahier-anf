import os
import re

cahier = open("_texts/raw.txt","r")
t = cahier.read()
s = re.compile("@@@ [0-9].* --").split(t)
fl = []

for filename in os.listdir("_cahier/"):
	fl.append(filename)

fl.sort()

n = 0

for segment in s:
	nf = open("_cahier/" + fl[n], "a")
	nf.write(segment)
	nf.close()
	n = n + 1