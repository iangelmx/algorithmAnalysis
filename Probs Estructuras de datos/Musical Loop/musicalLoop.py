try:
	linea = input("")
	while linea != "0":
		Nsamples = int(linea)
		rawSamples = input().split()
		samples = []
		for a in rawSamples:
			samples.append(int(a))

		#print("original",samples)
		lenSam = len(samples)
		samples = samples*2
		samples = samples[ (lenSam-1) :  ]
		samples.extend([samples[1]])
		estado=""
		anterior=""
		picos = 0
		for b in range(0, len(samples)-1):
			if samples[b+1] > samples[b]:
				anterior=estado
				estado = "sube"
			elif samples[b+1] < samples[b]:
				anterior = estado
				estado = "baja"

			if estado != anterior and anterior != "":
				picos +=1
		print(picos)
		#print("periodo de Interes->",samples)
		linea=input()





except Exception as ex:
	print(ex)
	pass