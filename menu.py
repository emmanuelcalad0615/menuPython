opcion = 99

while opcion != 3:
    print("***MENU***")
    print("1. saludar")
    print("2. despedir")
    print("3. salir")

    opcion=int(input("escriba la opcion"))
    if(opcion==2):
        print("Hasta luego")
    
else:
    print("termino")