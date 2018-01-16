import os, glob, json, sys, subprocess

#Create directory list to text file
userhome = os.path.expanduser('~')
dir_list = glob.glob(userhome + r'/local-repo/*')
print ("Found "+str(len(dir_list))+" directories")

with open ("dir_list.txt", mode="wt", encoding="utf-8") as myfile:
	myfile.write('\n'.join(dir_list))
print ("File dir_list.txt has been created")