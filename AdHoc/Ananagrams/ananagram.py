#from datetime import datetime
def verificaPalabras(ListaPalabras):
    ananagrams = []
    nPalabras = len(ListaPalabras)
    lenPal = len(ListaPalabras[0])
    #print("lista:",ListaPalabras)
    for palabra in ListaPalabras:
        existeTheSame = 0
        cumple=False
        for a in range(0, nPalabras): #Va checando palabra con las demás
            cont = 0
            if ListaPalabras[a] == palabra:
                #if ListaPalabras[a] == 'cole' and palabra == 'cole':
                #    print("Se compararía cole con cole")
                existeTheSame += 1
                continue
            wordToCheck = ListaPalabras[a]
            #if ListaPalabras[a] == 'aqua' and palabra == 'aqua':
                #print("Se compararía aqua con aqua")
            for char in palabra:
                if char not in wordToCheck: #Si cada caracter de palabra no está en la palabra a analizar
                    cont=0
                    #print("No encontro el char",char,"en",ListaPalabras[a])
                    break
                else:
                    wordToCheck=wordToCheck.replace(char,"",1)
                    cont+=1
                #if palabra == 'aqua':
                    #print("cont",cont)
            if cont >= lenPal:
                cumple=True
                break
        if cumple == False and existeTheSame <= 1:

            #print("Se appendeará", palabra)
            ananagrams.append(palabra)

    return ananagrams

try:
    #startTime = datetime.now()
    diccionarioPalabras = {}

    totalPalabras = []

    linea = input("")
    while linea != '#':
        palabras = linea.split()
        for palabra in palabras:
            diccionarioPalabras[ palabra ] = {'len':len(palabra), 'lower':palabra.lower()}
            totalPalabras.append(palabra)
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
                for a in range(0, totalPalabras.count(palabra)):
                    aux.append( diccionarioAux[palabra]['lower'] )

        listaPorLongitud[longitud] = aux
    
    ananagramsUlti = []
    #print("ListaPorLongitud:",listaPorLongitud)
    for key in listaLongitudes:
        #print("Llamara a verificaPalabras con:", listaPorLongitud[key])
        ananagramsUlti.extend( verificaPalabras( listaPorLongitud[key] ) )

    #print("Ananagrams Ulti:",set(ananagramsUlti))
    #ananagramsUlti = sorted(ananagramsUlti)
    ananagramsUlti = list(set(ananagramsUlti))

    llaves = list(sorted(diccionarioPalabras.keys()))

    for key in llaves:
        if diccionarioPalabras[key]['lower'] not in ananagramsUlti:
            continue
        else:
            print(key)

    #tiempo = datetime.now() - startTime
    #print(tiempo,"segs de exec")

except Exception as ex:
    #print(ex)
    pass