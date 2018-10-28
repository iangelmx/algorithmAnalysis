try:
    diccionario = {
        'W': 1,
        'H': 1/2,
        'Q': 1/4,
        'E': 1/8,
        'S': 1/16,
        'T': 1/32,
        'X': 1/64
    }
    line = input("")
    while(line != "" or line != "*"):
        measures = line.split("/")
        countCorrectMeasures = 0
        for measure in measures:
            medida = 0
            for note in measure:
                medida += diccionario[ note ]
            if medida == 1:
                countCorrectMeasures+=1
        print(countCorrectMeasures)
        line = input()

except Exception as ex:
    #print("Exception")
    #print(ex)
    pass