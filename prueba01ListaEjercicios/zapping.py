try:
	a = 0
	while True:
		a+=1
		[current, destination] = list(map(int,  input("").split() ))
		if current == -1 and destination == -1:
			break

		toUp = abs( destination - current )

		if destination > current:
			toDown = abs( current + 1 +(99 - destination) )
		else:
			toDown = abs( destination + 1 +(99 - current) )

		if toUp < toDown:
			print(toUp)
		else:
			print(toDown)

except Exception as ex:
	pass