import os
import re

chiens = open("chiens.txt","r")
t = chiens.read()
s = re.compile("\[.+blank'}").split(t)
fl = []

for filename in os.listdir("_chiens/"):
	fl.append(filename)

fl.sort()

n = 0

for segment in s:
	nf = open("_chiens/" + fl[n], "a")
	nf.write(segment)
	nf.close()
	n = n + 1