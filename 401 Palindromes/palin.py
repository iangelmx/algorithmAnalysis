try:
	espejo = {
		'A':'A',
		'E':'3',
		'H':'H',
		'I':'I',
		'J':'L',
		'L':'J',
		'M':'M',
		'O':'O',
		'S':'2',
		'T':'T',
		'U':'U',
		'V':'V',
		'W':'W',
		'X':'X',
		'Y':'Y',
		'Z':'5',
		'1':'1',
		'2':'S',
		'3':'E',
		'5':'Z',
		'8':'8'
	}

	##No es palíndromo
	##No es palíndromo, pero si se espejean los caracteres resulta ser igual

	#SI ES PALINDROMO:
	# Es un palíndromo regular, pero no se puede espejear
	# Es un palíndromo que también se puede espejear y da lo mismo

	linea = input("")
	a=0
	while(linea != ""):
		pInversa = linea[::-1]
		esPalindromo = False
		palFeatures = {
		'PAL_REG':False,
		'PAL_MIR':False
		}
		noPalFeatures = {
		'PAL_MIR':False
		}
		if pInversa == linea:
			esPalindromo = True
			palFeatures['PAL_REG'] = True
		else:
			esPalindromo = False

		if esPalindromo == True:
			mirrored = ""
			flagUsoEspejo=False
			for char in pInversa:
				if char in espejo:
					mirrored += espejo[char]
					flagUsoEspejo = True
				else:
					flagUsoEspejo = False
					break
					#mirrored += char

			#print("espejeda:",mirrored,"|original:",linea)
			if mirrored == linea and flagUsoEspejo == True:
				palFeatures['PAL_MIR'] = True

			if palFeatures['PAL_MIR'] == True:
				print(linea+" -- is a mirrored palindrome.")
			else:
				print(linea+" -- is a regular palindrome.")
		else:
			mirrored = ""
			for char in pInversa:
				if char in espejo:
					mirrored += espejo[char]
				else:
					mirrored += char
			if mirrored == linea:
				noPalFeatures['PAL_MIR'] = True

			if noPalFeatures['PAL_MIR'] == True:
				print(linea+" -- is a mirrored string.")
			else:
				print(linea+" -- is not a palindrome.")
			#print(pInversa+" <-> "+linea+" - is a ")
		print("")
		linea = input()

except Exception as ex:
	#print(ex)
	pass