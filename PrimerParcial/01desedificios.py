from datetime import datetime
startTime = datetime.now()
#N = int(input(""))
N = eval(raw_input())
#alturas = list(map(int, input("").split()))
alturas = map(int, raw_input().split())

alturas = [0]+alturas+[0]
maximo = 0
area = 0
Pa = [0]
Pi = [0]

for i in range(1, N+2):
	if alturas[i] > Pa[-1]:
		Pa.append( alturas[i] )
		Pi.append( i )
	while alturas[i] < Pa[-1] :
		area = Pa[-1] * (i - Pi[-1])
		maximo = max(area, maximo)
		Pa.pop()
		if alturas[i] > Pa[-1]:
			Pa.append( alturas[i] )
		else:
			Pi.pop()
print maximo
print datetime.now() - startTime 