try:
	linea = input("")
	while linea != "":
		testCases = int(linea)
		for a in range(0, testCases):
			n = int( input("") )
			nums = list(map(int,  input("").split() ))
			monedasObtenidas = {}
			for num in nums:
				monedasObtenidas[num]=False

			#print(nums)
			suma = sum(nums)
			print(suma)
			while suma > 0:
				aux = int(suma / (nums[-1]))
				#print(aux)
				if aux > 0:
					monedasObtenidas[nums[-1]] = True
					#print("Entró a if aux > 0")
				suma = suma % int(nums[-1])
				#print("Nuevo valor suma->", suma)
				nums.pop()
			print(monedasObtenidas)
			cuenta = 0
			for moneda in monedasObtenidas:
				if monedasObtenidas[moneda] == True:
					cuenta+=1
			print(cuenta)
		linea = input()
except Exception as ex:
	#print(ex)
	pass