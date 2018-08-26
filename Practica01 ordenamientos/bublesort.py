#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

archivo = open("salida.txt", "a+")

startTime = datetime.now()
#N = eval(raw_input(""))
N = int(input(""))
#lista = raw_input ("")
lista = input("")
nums=[]
lista = lista.split()
for elem in lista:
	nums.append(eval(elem))
for j in range(0, N-1):
	for a in range(0, N-1):
		if(nums[a] > nums[a+1]): #Codigo de correccion
			swap = nums[a]
			nums[a] = nums[a+1]
			nums[a+1] = swap
print(' '.join(str(a) for a in nums)+' \n')
tiempo = datetime.now() - startTime
archivo.write(str(N)+",")
archivo.write(str(tiempo)+"\n")
archivo.close()