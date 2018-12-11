try:
    linea = input("")
    while linea != "0 0 0":
        [n, d, r] = list(map(int, linea.split()))
        morningRoutes = list( map(int, input("").split()) )
        eveningRoutes = list( map(int, input("").split()) )

        morningRoutes = sorted(morningRoutes,reverse=True)
        eveningRoutes = sorted(eveningRoutes)
        #print("morning:",morningRoutes)
        #print("evening:",eveningRoutes)

        b = len(morningRoutes)
        drivers = [0] * b

        for a in range(0, b):
            drivers[a] = morningRoutes[a]+eveningRoutes[a]
        
        #print(drivers)

        pagosExtra = 0

        for lenghtRoute in drivers:
            if lenghtRoute > d:
                pagosExtra += (lenghtRoute -d ) * r
        
        #print("Pagos extra:", pagosExtra)
        print(pagosExtra)

        linea = input("")

except Exception as ex:
    print(ex)
    pass