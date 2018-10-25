try:
	while(True):
		cadena = ""
		strIn = input("")
		flag = "fin"
		auxInicio=""
		for char in strIn:
			if char == '[':
				flag = "inicio"
				a= 0
			elif char == ']':
				flag = "fin"
				a=0
			elif char != '[' or char != ']':
				if flag == "inicio":
					auxInicio += char
				else:
					cadena = auxInicio + cadena
					auxInicio=""
					cadena = cadena + char
			else:
				pass
		print(cadena)
except Exception as ex:
	#print(ex)
	pass