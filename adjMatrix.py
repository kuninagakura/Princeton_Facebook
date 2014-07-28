# Kuni Nagakura
# adjMatrix.py
# Print the adjacency matrix of the social graph

import pickle

graphList = pickle.load(open("PrincetonGraph2.p", "rb"))
# print graphList
names = pickle.load(open("PrincetonNames2.p", "rb"))

bindings = {}
nodeList = {}
#make dictionary for index bindings for all the users
i = 0
for key in graphList:
	if key not in bindings.keys():
		bindings[key] = i
		i += 1
	for fID in graphList[key]:
		if fID not in bindings.keys():
			bindings[fID] = i
			i += 1

adjMatrix = [[0 for x in range(i)] for y in range(i)] 

for key in graphList:
	for fID in graphList[key]:
		adjMatrix[bindings[key]][bindings[fID]] = 1
		adjMatrix[bindings[fID]][bindings[key]] = 1

for j in range(len(adjMatrix)):
	print adjMatrix[j]
