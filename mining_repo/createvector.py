#Create committer vector
#Produce csv vector file of the committer

import os, subprocess, glob, sys, json, csv, operator
from itertools import chain

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

project = [val.get('com_num') for sublists in data.values() for val in sublists]
dev = [val.get('email') for sublists in data.values() for val in sublists]

#remove duplicate value in list
project = set(project)
project = list(project)
project.sort()
dev = set(dev)
dev = list(dev)
dev.sort()

print ("No. of project : " + str(len(project)))
print ("No. of dev     : " + str(len(dev)))

#frequency of developer
sortdev = sorted(chain.from_iterable(data.values()), key=lambda x: x['email'], reverse=True)

no_dev = []
for i in range(0, len(dev)):
	no_dev.append(0)

c = 0
for n in project:
	if n in data:
		c = c + 1
		sys.stdout.write("\rCount on Project : %i" %(c))
		sys.stdout.flush()
		for p in data[n]:
			if p['email'] in dev:
				ind = dev.index(p['email'])
				no_dev[ind] = no_dev[ind]+1

dev_freq = []
dev_freq.append(dev)
dev_freq.append(no_dev)

#write to csv file
with open(userhome + r'/local-repo/mining_repo/devfreq.csv', 'w') as csvfile:
	writers = csv.writer(csvfile)
	for i in range(0, len(dev_freq)):
		writers.writerow(dev_freq[i])
	csvfile.close()
print("File devfreq.csv has been created")