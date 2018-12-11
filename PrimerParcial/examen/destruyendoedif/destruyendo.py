class Pila():
	altura = 0
	posicion = 0

edificios = [None]*1000005
pilas = [Pila()]*1000005

tope = -1
areaMaxima = 0
n=0
def confirma(area):
	global areaMaxima
	if area > areaMaxima:
		areaMaxima=area

def main():
	global tope
	n=eval(raw_input())
	#for i in range(0, n):
	#	edificios[i] = eval(raw_input())
	edificios = map(int, raw_input().split())

	edificios.append(0)
	tope+=1
	pilas[tope].posicion = 0
	pilas[tope].altura = edificios[0]
	for i in range(n+1):
		altura=edificios[i]
		if altura>= pilas[tope].altura:
			tope+=1
			pilas[tope].altura=altura
			pilas[tope].posicion=i
		else:
			while pilas[tope].altura >= altura and tope>=0:
				diferencia = i - pilas[tope].posicion
				a = diferencia * pilas[tope].altura
				confirma(a)
				tope-=1
			tope+=1
			pilas[tope].altura=altura
	print str(areaMaxima)


if __name__ == '__main__':
	main()
