try:
	line = input("")

	while line != None and line != "":
		print(line)
		line = input("")
except EOFError as ex:
	pass