# Kuni Nagakura
# getGraph.py
# Main webscraper for getting Facebook friendship lists
# cross references a dictionary of enlisted students and builds
# a social graph with the scraped information. Facebook users are keyed
# by Facebook User ID, and names are recorded using a dictionary that is 
# pickled for subsequent use of the data

from bs4 import BeautifulSoup
from mechanize import Browser
import re
from sets import Set
import pickle
import csv

mec = Browser()
mec.set_handle_robots(False)
userID = "1380180447"
graphList = {} #the graph
unexploredSet = Set() #unexplored users
exploredSet = Set() #explored users
names = {}

#add root user to name dictionary
names[userID] = "Kuni Nagakura"

#get set of enrolled students and put them in studentDictionary
studentDictionary = Set()
with open('students.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		firstName = row[0]
		lastName = row[1]
		studentDictionary.add(firstName + lastName)

#add root user to exploredSet
exploredSet.add(userID)
studentDictionary.remove("KuniNagakura")

url = "https://www.facebook.com/ajax/typeahead_friends.php?u=" + userID + "&__a=1"
page = mec.open(url)
html = page.read()
soup = BeautifulSoup(html)

text = soup.prettify()
#get all the friends of the root user
friends = text.split('{')
for friend in friends:
	#retrieve a friend 
	splitFriend = friend.split(",")
	#make sure it's a full entry
	if (len(splitFriend) > 2):
		#obtain Name, ID, and Key
		friendName = splitFriend[0].strip("\"t\"\:\"")
		friendID = splitFriend[1].strip("\"i\"\:")
		friendKey = ""
		#make sure key isn't corrupt and assign proper value
		if (len(friendName) > 2 and len(friendName.split(" ")) >= 2): 
			friendKey = friendName.split(" ")[0] + friendName.split(" ")[1]

		if friendKey in studentDictionary:
			if graphList.has_key(userID):
				graphList[userID].append(friendID)
			else:
				graphList[userID] = [friendID]
			#add to unexplored set
			unexploredSet.add(friendID)
			studentDictionary.remove(friendKey)
			names[friendID] = friendName

# while there are still users in the unexplored set
while len(unexploredSet):
	print len(unexploredSet)

	#get the first user ID in unexplored set
	exploreID = unexploredSet.pop()
	#add the first user ID to explored Set
	exploredSet.add(exploreID)

	#get the name and key of explored user ID
	exploreName = names[exploreID]
	print exploreName
	exploreKey = ""
	if (len(exploreName) > 2 and len(exploreName.split(" ")) >= 2): 
		exploreKey = exploreName.split(" ")[0] + exploreName.split(" ")[1]
	
	url2 = "https://www.facebook.com/ajax/typeahead_friends.php?u=" + exploreID + "&__a=1"
	page2 = mec.open(url2)
	html2 = page2.read()
	soup2 = BeautifulSoup(html2)

	text2 = soup2.prettify()
	#get the explored user's friends
	friends2 = text2.split('{')
	for friend in friends2:
		#retrieve friend
		splitFriend = friend.split(",")
		if (len(splitFriend) > 2):
			#get the name, id, and key
			friendName = splitFriend[0].strip("\"t\"\:\"")
			friendID = splitFriend[1].strip("\"i\"\:")
			friendKey = ""
			re.sub(r'\_', '', friendName)
			if (len(friendName) > 2 and len(friendName.split(" ")) >= 2): 
				friendKey = friendName.split(" ")[0] + friendName.split(" ")[1]

			#check that the friendkey is in student dictionary or unexplored (ie. alreadyin graphlist)
			#if he/she is, then add to/update the graphlist with current friend
			if (friendKey in studentDictionary or friendID in unexploredSet or friendID in exploredSet):
				# print exploreName + " " + friendName
				#if the explored user has been added to the graphlist already, then append
				if graphList.has_key(exploreID):
					graphList[exploreID].append(friendID)
				#the explored user has not been added, so add new node and assign first friend. 
				else:
					graphList[exploreID] = [friendID]

				#if this friendKey is in the student dictionary, add to unexplored and remove 
				if friendKey in studentDictionary:
					# print "new unexplored: " + friendName
					#add to unexplored
					unexploredSet.add(friendID)
					#remove the student's name from student dictionary
					studentDictionary.remove(friendKey)
					#add friend to name dictionary
					names[friendID] = friendName



pickle.dump(graphList, open("PrincetonGraph3.p", "wb"))
pickle.dump(names, open("PrincetonNames3.p", "wb"))
#print len(graphList)
#print studentDictionary



