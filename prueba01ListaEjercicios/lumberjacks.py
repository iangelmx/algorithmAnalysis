try:
	N = int( input("") )
	print("Lumberjacks:")
	for a in range(0, N):
		flag = False
		lista = list(map(int,  input("").split() ))
		if sorted(lista) == lista:
			flag = True
		elif sorted(lista, reverse=True) == lista:
			flag = True
		if flag == True:
			print("Ordered")
		else:
			print("Unordered")
except Exception as ex:
	print(ex)
	pass