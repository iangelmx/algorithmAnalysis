import time
try:
	while True:
		[N, B, H, W] = list(map(int, input("").split()))
		preciosHoteles = []
		for a in range(0, H):
			flag = False		
			precioHotel = int(input())
			camasDisponibles = list(map(int, input("").split()))
			costoPre = precioHotel * int(N)
			preciosHoteles.append(costoPre)
		try:
			precioMinimo = min(preciosHoteles)
		except:
			precioMinimo = 9999999999

		if precioMinimo > B:
			flag = False
		else:
			flag = True
		if flag == False:
			print("stay home")
		else:
			print(precioMinimo)
except Exception as ex:
	pass
