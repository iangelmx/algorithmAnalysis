def divideArreglo(arr):
	longitud = len(arr)
	if longitud <= 1:
		return arr

	limiteA = len(arr)//2

	mitadIzq = arr[  : limiteA]
	mitadDer = arr[limiteA:  ]

	divideArreglo(mitadIzq)
	divideArreglo(mitadDer)
	
	a=0
	b=0
	k=0

	while a < len(mitadIzq) and b < len(mitadDer):
		if mitadIzq[a] < mitadDer[b]:
			arr[k]=mitadIzq[a]
			a=a+1
		else:
			arr[k]=mitadDer[b]
			b=b+1
		k=k+1

	while a < len(mitadIzq):
		arr[k]=mitadIzq[a]
		a=a+1
		k=k+1

	while b < len(mitadDer):
		arr[k]=mitadDer[b]
		b=b+1
		k=k+1
	

def mergeSort(arr):
	divideArreglo(arr)

if __name__ == '__main__':
	arr = [8,2,40,36,21]
	print(arr)
	mergeSort(arr)
	print(arr)
	print("...")