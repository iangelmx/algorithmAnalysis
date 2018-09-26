"""DFT and FFT"""
import math

def expI(n): #e^(i*n)
	return complex(math.cos(n), math.sin(n))

def dft(Xn):
	N = len(Xn)
	arreglo = []
	for i in range(0,N): #0 a N-1
		acum = 0
		for k in range(0, N):
			acum+= Xn[k] * expI(-2 * math.pi * i * k / N)
		arreglo.append(acum)
	return arreglo

# def dft(xs):
#     "naive dft"
#     n = len(xs)
#     return [sum((xs[k] * iexp(-2 * math.pi * i * k / n) for k in range(n)))
#             for i in range(n)]

"""def dftinv(Xn):
	"naive dft"
	n = len(Xn)
	return [sum((Xn[k] * expI(2 * math.pi * i * k / n) for k in range(n))) / n
			for i in range(n)]"""

if __name__ == "__main__":
	wave = [0, 1, 2, 3, 3, 2, 1, 0]
	dfreq = dft(wave)
	#dwave = dftinv(dfreq)
	print(dfreq)
	#print([v.real for v in dwave])
	pass