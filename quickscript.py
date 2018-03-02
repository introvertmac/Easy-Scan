
newFile = open("adminLogins2.txt", 'w')
with open("adminLogins.txt", 'r') as f:
	for line in f.readlines():
		newFile.write(line.replace(',', '\n'))