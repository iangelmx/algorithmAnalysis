from random import randint

for a in range(1, 101):
	N = a*60
	filename = "in_"+str(a)+".txt"
	archivo = open(filename, 'w')

	cadena = ""
	for a in range(0, N):
		cadena += str( randint(-1000, 1000) )+" "

	cadena = cadena[:-1]

	archivo.write(str(N)+"\n")
	archivo.write(cadena)
	archivo.close()