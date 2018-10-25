try:
	testCases = int(input(""))
	for a in range(0, testCases):
		farmers = int( input("") )
		prima = 0
		for b in range(0,farmers):
			[space, animals, ecofriend] = list(map(int,  input("").split() ))
			prima += space*ecofriend
		print(prima)
except Exception as ex:
	pass
