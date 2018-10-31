import os

def goToStartOfLine():
    global x
    #print("Vino a gotoStartOfline")
    x=0

def clearScreen():
    global matrizLineal
    #print("Vino a clearScreen")
    matrizLineal = [" "] * 100

def moveOneRow(direction):
    print("Movió Row a la", direction)
    global y
    if direction == "up":
        if y > 0:
            y = y - 1
    else: #It goes down
        if y < 9:
            y = y + 1

def eraseToRight():
    #print("Vino a eraseToRight")
    global matrizLineal, x, y
    cursorPosition = (y*10) + x
    matrizLineal[ cursorPosition ] = " "
    aux = matrizLineal[:cursorPosition]
    auxFin = matrizLineal[cursorPosition: ]
    matrizLineal = aux.extend(auxFin)
    matrizLineal.extend([' '])


def goToOrigin():
    global x, y
    #print("Vino a origen")
    x = 0
    y = 0

def changeToInsertMode():
    #print("cambio escritura a INSERT")
    global writeMode
    writeMode = "insert"

def moveOneColumn(direction):
    #print("Se movió X a la", direction)
    global x
    if direction == "left":
        if x > 0:
            x = x - 1
    else: #It goes right
        if x < 9:
            x = x + 1

def chageToOverwriteMode():
    #print("cambio Escritura a OVERWRITE")
    global writeMode
    writeMode = "overwrite"

def circunflex():
    #print("Escribió un ^")
    global matrizLineal, x, y
    cursorPosition = (y*10) + x
    matrizLineal[ cursorPosition ] = "^" 

def moveToXY(row, column):
    global x, y
    x = column
    y = row
    print("Movió el cursor Y,X a: (", y,",", x,")")

def printMatrix():
    global matrizLineal
    strOut = "+----------+\n|"
    for b in range( len(matrizLineal) ):
        if b % 10 == 0 and b != 0:
            strOut += "|\n|"+matrizLineal[b]
        else:
            strOut += matrizLineal[b]
    strOut+="|\n+----------+"
    print(strOut)

def changeCoordinates(trace = False):
    global x, y
    if x < 9:
        x+=1
    elif y >=9 and x >= 9: #Checar si se va al origen o si se queda al final
        y = 9
        x = 9
    #if trace=="abc":
        #print("after ",y,",",x,")")


def writeToMatrix(char):
    global matrizLineal, x, y, writeMode

    cursorPosition = (y*10) + x
    print("current (",y,",",x,")")
    if writeMode == 'overwrite':
        #print("escribirá Estándo en overwrite")
        #print("posición: ",cursorPosition)
        matrizLineal[ cursorPosition ] = char
        printMatrix()    
        changeCoordinates(trace=True)
    else :
        print("Escribirá Estando en insert")
        startString = matrizLineal[ :cursorPosition]
        #print("startString",startString)
        saveEndString = matrizLineal[ cursorPosition: ] #Guarda a partir de la pos actual hasta el final
        #print("saveEndString",saveEndString)
        startString.extend([char]) #Le concatena el elemento
        #print("startString.extend",saveEndString)
        startString.extend( saveEndString[:-1] )
        matrizLineal = startString
        #print("matrizLineal",matrizLineal)
        printMatrix()
        changeCoordinates(trace=True)
        #matrizLineal[ cursorPosition ] = char #Escribe en la posición
        #matrizLineal[ cursorPosition+1 ] = saveEndString[:-1] #Escribe después de la 


def main():
    global writeMode, comandos, matrizLineal, x,y
    try:
        # ^## Move the cursor to the row and column specified;# represents a decimal digit; 
        # the first # represents the new row number, and the second # represents 
        # the new column number 
        N = input("")
        case = 0
        while N != "0":
            case += 1
            print("Case "+str(case))
            matrizLineal = [" "] * 100
            x=0
            y=0
            N = int(N)
            writeMode = "overwrite"
            for c in range( N ): #Va de 1 a N
                ###print("c->",c)
                linea = input()
                a=0
                #print(linea)
                #printMatrix()
                #for a in range( 0, len(linea) ):
                while a < len(linea):
                    ###print("char #"+str(a)+"->"+linea[a]+"<-")
                    if linea[a] == '^' and a < len(linea) - 1:
                        try:
                            x_new = int(linea[a+1])
                            #print("Se mandará: ",x_new,",",int(linea[a+2]))
                            moveToXY( x_new, int(linea[a+2]) )
                            a=a+3
                            #print("Era un numero")
                        except Exception as ex:
                            #print(ex)
                            #print("Llamará a: ^"+linea[a+1]) #+" a=",a)
                            if linea[a+1]=="d":
                                comandos[ "^"+linea[a+1] ]("down")
                            elif linea[a+1] == "u":
                                comandos[ "^"+linea[a+1] ]("up")
                            elif linea[a+1] == "l":
                                comandos[ "^"+linea[a+1] ]("left")
                            elif linea[a+1] == "r":
                                comandos[ "^"+linea[a+1] ]("right")
                            else:
                                comandos[ "^"+linea[a+1] ]() #Llama a la funcion
                            #printMatrix()
                            a=a+2
                            #print("a_post = ",a)
                            #print(".................")
                    else:
                        writeToMatrix(linea[a])
                        a=a+1
                        #printMatrix()
            N = input("")
            printMatrix()
        #print(matrizLineal)
        #print("")
    except Exception as ex:
        #printMatrix()
        #print(ex)
        pass

if __name__ == '__main__':
    matrizLineal = [" "] * 100
    #printMatrix()
    #printMatrix()
    x=0
    y=0
    writeMode = "overwrite"
    comandos ={
        '^b' : goToStartOfLine,#Move the cursor to the beginning of the current line; the cursor row does not change 
        '^c' : clearScreen,# Clear the entire screen; the cursor row and column do not change
        '^d' : moveOneRow,#^d Move the cursor down one row if possible; the cursor column does not change
        '^e' : eraseToRight, #Erase characters to the right of, and including, the cursor column on the cursor’s row; the cursor row and column do not change
        '^h' : goToOrigin, #Move the cursor to row 0, column 0; the image on the screen is not changed
        '^i' : changeToInsertMode, #Enter insert mode (see below)
        '^l' : moveOneColumn, #Move the cursor left one column, if possible; the cursor row does not change
        '^o' : chageToOverwriteMode, #Enter overwrite mode (see below) 
        '^r' : moveOneColumn, #Move the cursor right one column, if possible; the cursor row does not change
        '^u' : moveOneRow, #Move the cursor up one row, if possible; the cursor column does not change 
        '^^' : circunflex, #Write a circumflex in current cursor's location
    }
    main()
    

