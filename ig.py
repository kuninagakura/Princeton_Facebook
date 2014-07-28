# Kuni Nagakura
# ig.py
# Use igraph to generate a graph and calculate assortativity by degree and class
from igraph import *
import pickle

graphList = pickle.load(open("PrincetonGraph3.p", "rb"))
names = pickle.load(open("PrincetonNames3.p", "rb"))
allinfo = pickle.load(open("PrincetonStudentInfo.p", "rb"))

g = Graph()
for key in graphList:
    namesKey = names[key].split(' ')[0] + ' ' + names[key].split(" ")[1]
    if not namesKey == 'Arieh Mimran' and not namesKey == 'Sunny Xu' and not namesKey == 'Angela Xu':
        year = float(allinfo[namesKey][0])
        g.add_vertex(key, _class=year)


    for fID in graphList[key]:
        fIDKey = names[key].split(' ')[0] + ' ' + names[key].split(" ")[1]
        if not fIDKey == 'Arieh Mimran' and not fIDKey == 'Sunny Xu' and not fIDKey == 'Angela Xu':
            fIDyear = float(allinfo[fIDKey][0])
            g.add_vertex(fID,_class=fIDyear)

c = 0
for key in graphList:    
    for fID in graphList[key]:
        c +=1
        print c
        g.add_edge(key, fID)

print "assortativity", g.assortativity('_class')