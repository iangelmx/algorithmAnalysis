try:
    linea=input("")
    instrucciones = {}
    while linea != "":
        while linea != "#":
            indica, idInstr, tiempo = linea.split()
            instrucciones[ int(idInstr) ] = int(tiempo)
            linea = input()
        K = int(input(""))
        maxInstr = max(instrucciones.values())
        
        #print("Max Instr", maxInstr)
        a=0
        cont = 0
        daSalida =0
        listaSalida = []
        while True:
            a+=1
            #print(a)
            for key in instrucciones:
                if a%instrucciones[key]==0:
                    listaSalida.append(key)
                    #print("apendeó->",key)
            if len(listaSalida) >= 1:
                listaSalida = sorted(listaSalida)
                for elem in listaSalida:
                    print(elem)
                    cont+=1
                    #print("cont->",cont, "lenLista->",len(listaSalida))
                listaSalida=[]
            if cont >= K:
                break
        
except Exception as ex:
    #print(ex)
    pass