import re

def decodifica(codigo):
	if len(codigo) > 1:
		if codigo == "78":
			return "+"
		if codigo[-2:] == "35":
			return "-"

		patternNegative = r"35$"
		patternFailed = r"^9.*4$"
		patternNotComp = r"^190"

		if re.match( patternNegative, codigo ):
			return "-"
		elif re.match( patternFailed, codigo ):
			return "*"
		elif re.match( patternNotComp, codigo ):
			return "?"	

	elif len(codigo) == 1:
		if codigo == "1" or codigo == "4":
			return "+"

if __name__ == "__main__":
	try:
		nLineas = int(input(""))

		for a in range(0, nLineas):
			codigo = input("").strip()
			resultado = decodifica(codigo)
			if resultado is not None:
				last = resultado
			print( last )
	except Exception as ex:
		#print(ex)
		pass