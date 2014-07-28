# Kuni Nagakura
# addColumn.py
# Prepares the Class Year, Dorm, Hometown and Academic information for Gephi
import csv
import pickle

cdict = {}
ddict = {}
adict = {}
print "Id,Class,Dorm,AcademicPlan"
with open('FullStudent.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		if (len(row) > 2):
			first = row[0]
			last = row[1]
			_class = row[2]
			dorm = row[4]
			acadplan = row[5]
			nameKey = first +' ' + last
			cdict[nameKey] = _class
			ddict[nameKey] = dorm
			adict[nameKey] = acadplan

with open('findClassofStudents.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		nameKey = row[0].split(' ')[0] + ' '+ row[0].split(' ')[1]
		name = row[0]
		dorm = ''
		if len(ddict[nameKey].split(' ')) > 2:
			dorm = ddict[nameKey].split(' ')[1] + ' ' +ddict[nameKey].split(' ')[2] 
		print name + ',' + cdict[nameKey] + ',' + dorm + ',' +adict[nameKey].split(' ')[0]

