try:
    linea = input("")
    while linea != "":
        cursorPos = "fin"
        auxInicio = ""
        cadena = ""
        for letra in linea:
            if letra == '[':
                cursorPos = "inicio"
            elif letra == ']':
                cursorPos = "fin"
            else:
                if cursorPos == "fin" and auxInicio != "":
                    cadena = auxInicio + cadena
                    auxInicio = ""
                elif cursorPos == "fin" and auxInicio == "":
                    cadena += letra
                elif cursorPos == "inicio":
                    auxInicio += letra
        print(cadena)
        linea = input()

except Exception as ex:
    #print(ex)
    pass