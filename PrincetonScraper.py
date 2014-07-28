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
		if (len(friendName.split(" ")) > 2): 
			friendKey = friendName.split(" ")[0] + friendName.split(" ")[1]
		if friendKey in studentDictionary:
			if graphList.has_key(userID):
				graphList[userID].append(friendID)
			else:
				graphList[userID] = [friendID]
			unexploredSet.add(friendID)
			names[friendID] = friendName

# while there are still users in the unexplored set
while len(unexploredSet):
	# if (len(unexploredSet) > 1000):
	# 	full = True
	print len(unexploredSet)
	exploreID = unexploredSet.pop()
	# exploredSet.add(exploreID)
	exploreName = names[exploreID]
	exploreKey = ""
	if (len(exploreName) > 2 and len(exploreName.split(" ")) >= 2): 
		exploreKey = exploreName.split(" ")[0] + exploreName.split(" ")[1]
	url2 = "https://www.facebook.com/ajax/typeahead_friends.php?u=" + exploreID + "&__a=1"
	page2 = mec.open(url2)
	html2 = page2.read()
	soup2 = BeautifulSoup(html2)

	text2 = soup2.prettify()
	#just splits
	friends2 = text2.split('{')
	for friend in friends2:
		splitFriend = friend.split(",")
		if (len(splitFriend) > 2):
			friendName = splitFriend[0].strip("\"t\"\:\"")
			friendID = splitFriend[1].strip("\"i\"\:")
			friendKey = ""
			re.sub(r'\_', '', friendName)
			if (len(friendName) > 2 and len(friendName.split(" ")) >= 2): 
				friendKey = friendName.split(" ")[0] + friendName.split(" ")[1]
			#check that the friendkey is in student dictionary or explored (ie. alreadyin graphlist)
			#if he/she is, then add to/update the graphlist with current friend
			if friendKey in studentDictionary or friendID in graphList.keys():
				if graphList.has_key(exploreID):
					graphList[exploreID].append(friendID)
				else:
					# if exploreKey in studentDictionary:
					# 	studentDictionary.remove(exploreKey)
					graphList[exploreID] = [friendID]
				#if this friend is not in unexplored and not in the graphlist, then add to be explored explored
				if friendID not in unexploredSet and friendID not in graphList.keys() and friendKey in studentDictionary:
					print friendName
					unexploredSet.add(friendID)
					studentDictionary.remove(friendKey)
					names[friendID] = friendName




pickle.dump(graphList, open("PrincetonGraph.p", "wb"))
pickle.dump(names, open("PrincetonNames.p", "wb"))
len(graphList)
# for key in graphList:
# 	print names[key] + "\n"
# 	print [names[fID] for fID in graphList[key]] 


