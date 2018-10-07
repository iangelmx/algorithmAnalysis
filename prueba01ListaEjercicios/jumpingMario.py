try:
	#out = open("salida_jumping.txt", "w")
	testCases = int( input("") )
	for a in range(0, testCases):
		walls = int( input("") )
		heights = list(map(int,  input("").split() )) #Se genera la lista de alturas
		HJ = 0
		LW = 0
		for b in range(1, walls):
			if heights[b] > heights[b-1]:
				HJ += 1
			elif heights[b] < heights[b-1]:
				LW += 1
			else:
				pass
		salida = "Case "+str(a+1)+": "+str(HJ)+" "+str(LW)
		#out.write(salida+"\n")
		print(salida)
	#out.close()
except Exception as ex:
	#print(ex)
	#out.close()
	pass