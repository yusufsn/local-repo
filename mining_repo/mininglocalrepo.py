import os, glob, json, sys, subprocess


print ("======================================")
#Create directory list to text file
userhome = os.path.expanduser('~')
dir_list = glob.glob(userhome + r'/local-repo/*')
print ("Found "+str(len(dir_list))+" directories")

with open ("dir_list.txt", mode="wt", encoding="utf-8") as myfile:
	myfile.write('\n'.join(dir_list))
print ("File dir_list.txt has been created")

proj = {}
for i in range(0, len(dir_list)):
	try:
		dirs = dir_list[i]
		os.chdir(dirs)
		p = subprocess.Popen('git log --pretty=%cE | sort | uniq -c | sort', 
			shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		dir_name = str(dir_list[i]).replace(userhome + r'/local-repo/',"")
		proj[dir_name] = []
		out = p.stdout.readlines()
		sys.stdout.write("\rExtracting features from files : %i " % (i+1))
		sys.stdout.flush()
		if out != []:
			for line in out:
				temp = line
				temp2 = str(temp).replace("b'","").replace("\\n'","").replace("  ","").split(' ')
				if '' == temp2[0]:
					temp2.remove(temp2[0])
				proj[dir_name].append({
					'com_num': temp2[0],
					'email': str(temp2[1])
					})
			retval = p.wait()
		else:
			proj[dir_name].append({
				'com_num': 0,
				'email': "-"
				})
	except Exception as e:
		print (" --> Found error on " + str(dir_list[i]).replace(userhome + r"/local-repo/"))

#creating json file
with open(userhome + r'/local-repo/mining_repo/committer.json', 'w') as fjson:
	json.dump(proj, fjson)
print ("\nFile committer.json has been created")

print ("======================================")