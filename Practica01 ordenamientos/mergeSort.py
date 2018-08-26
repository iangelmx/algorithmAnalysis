#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

archivo = open("salida2.csv", "a+")

startTime = datetime.now()
def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

alist = []
N = int(input(""))
nums = input("").split()
for a in nums:
    alist.append(int(a))
mergeSort(alist)
print(' '.join(str(a) for a in alist)+' \n')
tiempo = datetime.now() - startTime

archivo.write(str(N)+",")
archivo.write(str(tiempo)+"\n")
archivo.close()