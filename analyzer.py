# Kuni Nagakura
# analyzer.py
# Reads in the Social graph and analyzes the data by different metrics.
# Mainly, this code is used to ascertain how many students living in a certain
# dorm are friends with others living the same dorm. The code can easily by manipulated
# to obtain the data along other attributes (class, hometown, academic plan, etc. )

import pickle
from sets import Set
import networkx as nx
import csv

G = nx.Graph()
graphList = pickle.load(open("PrincetonGraph3.p", "rb"))
names = pickle.load(open("PrincetonNames3.p", "rb"))
allinfo = pickle.load(open("PrincetonStudentInfo.p", "rb"))
_class = {}
address = {}
city = {}
acadplan = {}

print 'name', 'class', 'dorm', 'samedorm', 'diffdorm'
node = Set()
edge = Set()
for key in graphList:

	namesKey = names[key].split(' ')[0] + ' ' + names[key].split(" ")[1]

	if not namesKey == 'Arieh Mimran' and not namesKey == 'Sunny Xu' and not namesKey == 'Angela Xu':
		G.add_node(key, name=namesKey, info=allinfo[namesKey])

	for fID in graphList[key]:
		G.add_node(fID)
		G.add_edge(key, fID)
		G.add_edge(fID, key)


nodes = nx.nodes_iter(G)

for n in nodes:
	#get list of neighbors
	neighbors = nx.all_neighbors(G, n)
	#initialize counters
	cSame = 0
	cDiff = 0
	nFriends = 0
	nKey = names[n].split(' ')[0] + ' ' + names[n].split(" ")[1]
	if not nKey == 'Arieh Mimran' and not nKey == 'Sunny Xu' and not nKey == 'Angela Xu' and not nKey == 'Elena Slobodyan':
		n_class = allinfo[nKey][0]
		n_dorm = ''
		if len(allinfo[nKey][1].split(',')) > 1:

			n_dorm = allinfo[nKey][1].split(',')[1] 
	for m in neighbors:
		nFriends +=1
		mKey = names[m].split(' ')[0] + ' ' + names[m].split(" ")[1]
		if not mKey == 'Arieh Mimran' and not mKey == 'Sunny Xu' and not mKey == 'Angela Xu' and not mKey == 'Elena Slobodyan':
			m_class = allinfo[namesKey][0]
			m_dorm = ''
			if len(allinfo[namesKey][1].split(',')) > 1:
				m_dorm = allinfo[namesKey][1].split(',')[1] 
		
		if m_dorm == n_dorm: 
			cSame += 1
		else: 
			cDiff += 1

	print names[n], n_class, n_dorm, cSame, cDiff, nFriends

		# m_city = G.node[m]['allinfo'][1]
		# m_address = G.node[m]['allinfo'][2]
		# m_acadplan = G.node[m]['allinfo'][3]

