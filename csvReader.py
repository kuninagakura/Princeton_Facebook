# Kuni Nagakura
# csvReader.py
# tool to read csv Files for importing into Gephi
import csv
from sets import Set

studentDictionary = Set()
with open('students.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		firstName = row[0]
		lastName = row[1]
		studentDictionary.add(firstName[0] + firstName[1] + lastName)
print studentDictionary