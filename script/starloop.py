i = str(raw_input('Input your character : '))
for x in range(5):
	for y in range(5):
		if y<=x:
			print i,
		else:
			print '',
	print('\n')