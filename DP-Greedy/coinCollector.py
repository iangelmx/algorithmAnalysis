try:
	linea = input("")
	while linea != "":
		testCases = int(linea)
		for a in range(0, testCases):
			n = int( input("") )
			nums = list(map(int,  input("").split() ))
			print(nums)
		linea = input()
except Exception as ex:
	print(ex)
	pass