try:
	testCases = int( input("") )
	salida = open("out_google.txt", "w")
	cadena = ""
	for a in range(0, testCases):
		print("Case #"+str(a+1)+":")
		salida.write("Case #"+str(a+1)+":\n")
		webs = []
		relevance = []
		for b in range(0, 10):
			webRelevance = input("").split()
			webs.append( webRelevance[0] )
			relevance.append( int(webRelevance[1]) )

		maximo = max(relevance)

		#print(webs)

		for c in range(0, len(webs) ):
			if relevance[c] == maximo:
				print(webs[c])
				salida.write(webs[c]+"\n")
	salida.close()
except Exception as ex:
	salida.close()
	print(ex)
	pass