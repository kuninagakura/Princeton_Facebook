# Kuni Nagakura
# getMoreInfo.py
# Web scraper for Princeton college facebook to get an enlisted student directory
# and information for analysis
from bs4 import BeautifulSoup
from mechanize import Browser
import re
from sets import Set
import pickle
import csv
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  

browser = webdriver.Firefox()  
browser.get('https://www.princeton.edu/collegefacebook/search/?order=last_name&sort=asc&view=list&page=6&limit=1000')  
html_source = browser.page_source 
soup = BeautifulSoup(html_source)
firstnames = soup("td", {"class":"firstname"})
lastnames = soup("td", {"class":"lastname"})
homecity = soup("td", {"class":"city"})
dorm = soup("td", {"class":"address"})
_class = soup("td", {"class": "class"})
acadplan = soup("td", {"class": "acadplan"})

for fn in firstnames:
	print fn
for ln in lastnames:
	print ln
for hc in homecity:
	print hc
for dm in dorm:
	print dm
for cl in _class:
	print cl
for ap in acadplan:
	print ap




