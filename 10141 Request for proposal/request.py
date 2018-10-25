import operator

try:
	linea = input("")
	propuestaNum = 0
	while(linea != "0 0"):
		propuestaNum+=1
		maximo = 0
		compliances = {} #guardará compliances
		precios = {}
		[n, p] = linea.split() # p es el número de propuestas, n son los req. Totales
		n = int(n)
		p = int(p)
		for a in range(0, n):
			linea = input() #Ignore :v x2
		for a in range(0, p):
			proposalName = input() #Leemos el nombre de la propuesta
			[precio, reqCump] = input().split()
			reqCump = int(reqCump)
			compliance = reqCump/n #n-> Req totales
			#Podría ser que haya fracciones muy cercanas
			compliances[proposalName] = compliance
			precios[proposalName] = float(precio)
			for b in range(0, reqCump):
				linea = input() #Ignore :v
		linea = input()
		maximo = max(compliances.values())

		possibleKeys = []
		for a in compliances:
			if compliances[a] == maximo: #cuántas compliances ='s hay?
				possibleKeys.append(a)
				ultimateKey = a

		if len(possibleKeys)> 1:
			print(possibleKeys)
			precios2 = {}
			for key in possibleKeys:
				precios2[key] = precios[key]
			minimo = min( precios2.values()  )
			#Checar si siguen en el mismo orden
			for a in precios:
				if(precios[a]==minimo):
					ultimateKey = a


		print("RFP #"+str( propuestaNum ) )
		print(ultimateKey)

except EOFError as ex:
	print(ex)
	print(":(")
