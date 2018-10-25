

try:
	out = open("out_specialHappy.txt", "w")
	n = int( input("") ) # Num de Invitados
	song = [
		"Happy","birthday","to","you","Happy","birthday","to","you",
		"Happy","birthday","to","Rujia",
		"Happy","birthday","to","you"
	]
	invitados = []
	for a in range(0, n):
		invitados.append( input("") )

	if len(invitados) < 16:
		b=0
		for a in range(0, len(song)):
			if b == len(invitados):
				b = 0
			print(invitados[b]+": "+song[a])
			out.write(invitados[b]+": "+song[a]+"\n")
			b+=1
	else:
		vecesCancion = len(invitados) // 16
		if len(invitados) % 16 != 0:
			vecesCancion += 1

		a = 0
		b = 0
		for c in range(0, len(song) * vecesCancion):
			if b == len(invitados):
				b = 0
			if a == len(song):
				a = 0
			print(invitados[b]+": "+song[a])
			out.write(invitados[b]+": "+song[a]+"\n")
			a+=1
			b+=1
	out.close()
except Exception as ex:
	out.close()
	print(ex)
	pass