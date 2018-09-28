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
#	 "naive dft"
#	 n = len(xs)
#	 return [sum((xs[k] * iexp(-2 * math.pi * i * k / n) for k in range(n)))
#			 for i in range(n)]

"""def dftinv(Xn):
	"naive dft"
	n = len(Xn)
	return [sum((Xn[k] * expI(2 * math.pi * i * k / n) for k in range(n))) / n
			for i in range(n)]"""
def is_pow2(n):
	return False if n == 0 else (n == 1 or is_pow2(n >> 1))

def fft_(xs, n, start=0, stride=1):
	"cooley-turkey fft"
	if n == 1:
		return [xs[start]]
	hn, sd = n // 2, stride * 2
	rs = fft_(xs, hn, start, sd) + fft_(xs, hn, start + stride, sd)
	for i in range(hn):
		e = expI(-2 * math.pi * i / n)
		rs[i], rs[i + hn] = rs[i] + e * rs[i + hn], rs[i] - e * rs[i + hn]
		pass
	return rs

def fft(xs):
	assert is_pow2(len(xs))
	return fft_(xs, len(xs))

if __name__ == "__main__":
	wave = [0, 1, 2, 3, 3, 2, 1, 0]
	dfreq = dft(wave)
	#dwave = dftinv(dfreq)
	print(dfreq)
	#print([v.real for v in dwave])
	pass