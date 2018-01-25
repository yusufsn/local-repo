#Create committer vector
#Produce csv vector file of the committer

import os, subprocess, glob, sys, json, csv, operator

def is_int(x):
	try:
		int(x)
		return True
	except ValueError:
		return False

#load project list from text file
userhome = os.path.expanduser('~')

txtfile = open("dir_list.txt", "r")
dir_list = txtfile.read().replace(userhome + r'/local-repo/mining_repo/',"").split('\n')
print("Found " + str(len(dir_list)) + " directories")

#create table header
jsonfile = userhome + r'/local-repo/mining_repo/committer.json'

#read committer from json file
with open(jsonfile, 'r') as js:
	data = json.load(js)

print(data)