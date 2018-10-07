
def calculaTarifa(plan, duracionLlamada):
	juice = 0
	mile = 0
	if plan == "juice":
		juiceAux = duracionLlamada // 120
		juice += juiceAux * 30
		juiceAux = duracionLlamada % 120
		if juiceAux >= 60:
			juice += 30
		else:
			juice += 15

		return juice
	elif plan == "mile":
		mileAux = duracionLlamada // 60
		mile += mileAux * 20
		mileAux = duracionLlamada % 60
		if mileAux >= 30:
			mile += 20
		else:
			mile += 10
		return mile
	else:
		pass

if __name__ == "__main__":
	try:
		testCases = int( input("") )
		for a in range(0, testCases):
			nCalls = int( input("") )

			milePrice = 0
			juicePrice = 0

			callsDuration = list(map(int,  input("").split() ))
			for call in callsDuration:
				duration = int(call)
				juicePrice += calculaTarifa("juice", duration)
				milePrice += calculaTarifa("mile", duration)

			#print("mile", milePrice)
			#print("juice", juicePrice)

			if juicePrice < milePrice:
				print("Case "+str(a+1)+": Juice "+str(juicePrice))
			elif milePrice < juicePrice:
				print("Case "+str(a+1)+": Mile "+str(milePrice))
			else:
				print("Case "+str(a+1)+": Mile Juice "+str(milePrice))

	except Exception as ex:
		print(ex)
		pass