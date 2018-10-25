import time
try:
	#salida = open("salida.txt", "w")
	#b=0
	while True:
		#b+=1
		[N, B, H, W] = list(map(int, input("").split()))
		preciosHoteles = []
		for a in range(0, H):
			flag = False		
			precioHotel = int(input())
			camasDisponibles = list(map(int, input("").split()))

			#print(camasDisponibles)
			#minimoCamasDisp = min(camasDisponibles)
			#print("camas minimas Disp:",minimoCamasDisp)
			#if minimoCamasDisp >= N:
				#print("Si hubo camas")
			costoPre = precioHotel * int(N)
			preciosHoteles.append(costoPre)
			#print("Anadio el precio->", precioHotel, "*", N, "=", costoPre)
			#else:
				#print("No hubo camas en este hotel")
				#pass
			#print("Fin hotel ",a)
		try:
			precioMinimo = min(preciosHoteles)
		except:
			precioMinimo = 9999999999

		if precioMinimo > B:
			flag = False
		else:
			flag = True
		if flag == False:
			#salida.write("stay home\n")
			#print("costoTotal->",precioMinimo)
			#print("preciosHoteles->", preciosHoteles)
			#print("...")
			#print("N, B, H, W->", N, B, H, W)
			print("stay home")
			#print("----------------------")
		else:
			#salida.write( str(precioMinimo)+"\n" )
			"""if b >= 29 and b <= 31:
				print("costoTotal->",precioMinimo)
				print("N, B, H, W->", N, B, H, W)
				print("...")
				print("preciosHoteles->", preciosHoteles)
				print("----------------------")"""
			print(precioMinimo)

		#time.sleep(5)
except EOFError as ex:
	pass
