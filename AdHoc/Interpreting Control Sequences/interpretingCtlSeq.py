def goToStartOfLine():
    global x
    x=0

def clearScreen():
    global matrizLineal
    matrizLineal = [None] * 100

def moveOneRow(direction):
    global y
    if direction == "up":
        if y > 0:
            y = y - 1
    else: #It goes down
        if y < 9:
            y = y + 1

def eraseToRight():
    global matrizLineal, x, y
    cursorPosition = (y*10) + x
    matrizLineal[ cursorPosition ] = " " 


def goToOrigin():
    global x, y
    x = 0
    y = 0

def changeToInsertMode():
    global writeMode
    writeMode = "insert"

def moveOneColumn(direction):
    global x
    if direction == "left":
        if x > 0:
            x = x - 1
    else: #It goes down
        if x < 9:
            x = x + 1


def chageToOverwriteMode():
    pass

def circunflex():
    return '^'

def moveToXY(row, column):
    pass

def printMatrix():
    pass

def writeToMatrix(char):
    pass

def main():
    global writeMode
    try:
        comandos ={
            '^b' : goToStartOfLine(),#Move the cursor to the beginning of the current line; the cursor row does not change 
            '^c' : clearScreen(),# Clear the entire screen; the cursor row and column do not change
            '^d' : moveOneRow("down"),#^d Move the cursor down one row if possible; the cursor column does not change
            '^e' : eraseToRight(), #Erase characters to the right of, and including, the cursor column on the cursor’s row; the cursor row and column do not change
            '^h' : goToOrigin(), #Move the cursor to row 0, column 0; the image on the screen is not changed
            '^i' : changeToInsertMode(), #Enter insert mode (see below)
            '^l' : moveOneColumn("left"), #Move the cursor left one column, if possible; the cursor row does not change
            '^o' : chageToOverwriteMode(), #Enter overwrite mode (see below) 
            '^r' : moveOneColumn("right"), #Move the cursor right one column, if possible; the cursor row does not change
            '^u' : moveOneRow("up"), #Move the cursor up one row, if possible; the cursor column does not change 
            '^^' : circunflex(), #Write a circumflex in current cursor's location
        }

        # ^## Move the cursor to the row and column specified;# represents a decimal digit; 
        # the first # represents the new row number, and the second # represents 
        # the new column number 
        linea = input("")
        while linea != "":
            writeMode = "overwrite"
            for a in range( 0, len(linea) ):
                if linea[a] == '^' and a < len(linea) - 2:
                    try:
                        b = int(linea[a+1])
                    except Exception as ex:
                        pass
                    if b:
                        moveToXY( int(linea[a+1]), int(linea[a+2]) )
                        a=a+2
                    else:
                        comandos[ linea[a]+linea[a+1] ]
                else:
                    writeToMatrix(linea[a])
                        

                     


    except Exception as ex:
        print(ex)
        pass

if __name__ == '__main__':
    main()
    matrizLineal = [" "] * 100
    x=0
    y=0
    writeMode = "overwrite"
    

