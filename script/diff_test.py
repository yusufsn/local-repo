for file in files:
	#for getting file
	f=open(file,"r")
	next(f)
	
for i in range(0,1):
	f=open(files[i],"r")
	header=next(f).replace("\n","")