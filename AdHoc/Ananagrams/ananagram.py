from datetime import datetime
def verificaPalabras(ListaPalabras):
    ananagrams = []
    for palabra in ListaPalabras:
        for a in range(0, len(ListaPalabras)):
            if 

try:
    startTime = datetime.now()
    diccionarioPalabras = {}

    linea = input("")
    while linea != '#':
        palabras = linea.split()
        for palabra in palabras:
            diccionarioPalabras[ palabra ] = {'len':len(palabra), 'lower':palabra.lower()}
        linea = input()

    diccionarioAux = diccionarioPalabras

    listaLongitudes = []

    for palabra in diccionarioAux:
        listaLongitudes.append( diccionarioAux[palabra]['len'] )

    listaLongitudes = list(set(sorted(listaLongitudes)))

    #print(listaLongitudes)
    listaPorLongitud = {}

    for longitud in listaLongitudes:
        aux = []
        for palabra in diccionarioAux:
            if diccionarioAux[palabra]['len'] == longitud:
                aux.append(palabra)

        listaPorLongitud[longitud] = aux
    

    for key in listaLongitudes:
        verificaPalabras( listaLongitudes[key] )

    tiempo = datetime.now() - startTime
    print(tiempo,"segs de exec")

except Exception as ex:
    print(ex)
    pass