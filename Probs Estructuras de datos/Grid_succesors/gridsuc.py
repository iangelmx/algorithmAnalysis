def haceOperaciones(matrix):
	nuevaMatriz = [0]*9
	nuevaMatriz[0] = (matrix[3]+matrix[1])%2
	nuevaMatriz[1] = (matrix[0]+matrix[2]+matrix[4])%2
	nuevaMatriz[2] = (matrix[1]+matrix[5])%2
	nuevaMatriz[3] = (matrix[0]+matrix[4]+matrix[6])%2
	nuevaMatriz[4] = (matrix[1]+matrix[5]+matrix[7]+matrix[3])%2
	nuevaMatriz[5] = (matrix[2]+matrix[4]+matrix[8])%2
	nuevaMatriz[6] = (matrix[3]+matrix[7])%2
	nuevaMatriz[7] = (matrix[6]+matrix[4]+matrix[8])%2
	nuevaMatriz[8] = (matrix[7]+matrix[5])%2
	return nuevaMatriz


try:
	testCases = int(input(""))

	for a in range(0,testCases):
		input()
		matriz = []
		for b in range(0,3):
			renglon = input("")
			for char in renglon:
				matriz.append(int(char))

		contadorSuccessions=0
		while max(matriz) > 0:
			matriz = haceOperaciones(matriz)
			contadorSuccessions += 1

		contadorSuccessions-=1
		print(contadorSuccessions)


except Exception as ex:
	print(ex)
	pass