if __name__ == '__main__':
#try:
	[n,k] = raw_input().split()
	n = int(n)
	k = int(k)
	strRecorrido = raw_input().split()
	nrecorridos = ( n-k )+1
	maximo = -50010
	#vuelta = 0
	recorrido = []
	g=0

	for a in range(0, len(strRecorrido)):
		num = eval( strRecorrido[a] )
		recorrido.append(num)
		
	for a in range(0, n):
		if a > 0 and a < k:
			g+=( recorrido[a] - recorrido[a-1] )
	if g > maximo:
		maximo = g
	g -= recorrido[1]-recorrido[0]

	for a in range(1, (n-k)):
		g-=(recorrido[a] - recorrido[a-1])
		#print g
		g+= ( recorrido[a+k-1] - recorrido[a+k-2] )
		if g>maximo:
			maximo=g
		


	print maximo

	"""
	for b in range(0, nrecorridos):
		emocion = 0
		for a in range(0, k-1):
			emocion += recorrido[a+1+vuelta] - recorrido[a+vuelta]
		if emocion > maximo:
			maximo = emocion
		vuelta+=1
		print "k->"+str(k)+" nrecorridos"+str(b)+" = "+str(emocion)
	print(maximo)
	"""
#except Exception as ex:
#	print(ex)
#	pass