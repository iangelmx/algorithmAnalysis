archivo = open('entrada2.txt', 'w')

cadena=""
for a in range(0, 10000000):
	cadena += "10000000000 "

cadena = cadena[:-1]

archivo.write("10000000\n")
archivo.write(cadena)
archivo.close()


