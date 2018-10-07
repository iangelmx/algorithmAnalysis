try:
	f=0
	while(True):
		testCases = int( input("") )
		input("")
		for a in range(0, testCases):
			f+=1
			if(f>1):
				print("")
			nRows = int( input("") )
			rows = []
			for b in range(0, nRows):
				rows.append( list(map(int,  input("").split() )) ) #Se guardan las ROWS

			valoresSur = []
			valoresNorte = []

			for row in rows:
				valoresSur.append( row[0] )
				valoresNorte.append( row[1] ) #Los convertiremos en -Negativos

			for c in range(0, len(valoresNorte)):
				valoresNorte[c] = (valoresNorte[c] * (-1))

			valoresFinal = []

			for d in range(0, len(valoresNorte) ):
				suma = valoresNorte[d] + valoresSur[d]
				valoresFinal.append( suma )

			minimo = min(valoresFinal)
			maximo = max(valoresFinal)

			if minimo == maximo:
				print("yes")

			else:
				print("no")

			input("") #Por si hay más casos abajo
except Exception as ex:
	#print(ex)
	pass