# Kuni Nagakura
# pickleReader.py
# Tool for reading pickled files
import pickle

graphList = pickle.load(open("PrincetonGraph2.p", "rb"))
# print graphList
names = pickle.load(open("PrincetonNames2.p", "rb"))

for key in graphList:
	print names[key] + "\n"
	print [names[fID] for fID in graphList[key]] 

