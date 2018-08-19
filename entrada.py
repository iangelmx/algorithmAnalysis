archivo = open('entrada2.txt', 'w')

cadena=""
for a in range(0, 1000000):
	cadena += str(a)+" "

cadena = cadena[:-1]

archivo.write("1000000\n")
archivo.write(cadena)
archivo.close()


