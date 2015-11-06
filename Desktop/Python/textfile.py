x = 0

while x != "quit":

	x = raw_input("Press any key to run")

	file = open("newfile2.txt", "w")

	file.write(x)

	file.close()

