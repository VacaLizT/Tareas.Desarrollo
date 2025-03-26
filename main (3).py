print("Se podrán hacer las siguientes conversiones: ")

opcion="""
    1. Conversiones de monedas
    2. Conversiones de Temperatura
    3. Conversiones de Distancia
    
"""
print(opcion)
opcion=input("Seleccione que opción desea: ")

if opcion=="1":
    opcion1="""
        a. Convertir de Q a Euros
        b. Convertir de Q a Dólares
        c. Convertir de Q a Pesos
        d. Convertir de Pesos a Q
        e. Convertir de Pesos a Dólares
        f. Convertir de Pesos a Euros

    """
    print(opcion1)
    opcion1=input("Seleccione que opción desea: ")

    if opcion1=="a":
        dinero=float(input("Ingrese número de Quetzales: "))
        print(dinero*0.12)
    elif opcion1=="b":
        dinero=float(input("Ingrese número de Quetzales: "))
        print(dinero*0.13023)
    elif opcion1=="c":
        dinero=float(input("Ingrese número de Quetzales: "))
        print(dinero*2.62)
    elif opcion1=="d":
        dinero=float(input("Ingrese número de Pesos: "))
        print(dinero*0.38)
    elif opcion1=="e":
        dinero=float(input("Ingrese número de Pesos: "))
        print(dinero*0.049)
    elif opcion1=="f":
        dinero=float(input("Ingrese número de Pesos: "))
        print(dinero*0.045)
    else:
        print("Error")

elif opcion=="2":
    opcion2="""
        a. Convertir de °F a K
        b. Convertir de °F a °C
        c. Convertir de K a °C
        d. Convertir de K a °F

    """
    print(opcion2)
    opcion2=input("Seleccione que opción desea: ")

    if opcion2=="a":
        temperatura=float(input("Ingrese los grados en °F: "))
        print((temperatura + 459.67) * 5/9)
    elif opcion2=="b":
        temperatura=float(input("Ingrese los grados en °F: "))
        print((temperatura - 32) * 5/9)
    elif opcion2=="c":
        temperatura=float(input("Ingrese los grados en K: "))
        print(temperatura-273.15)
    elif opcion2=="d":
        temperatura=float(input("Ingrese los grados en K: "))
        print((temperatura*9/5) - 459,67)
    else:
        print("Error")
        
elif opcion=="3":
    opcion3="""
        a. Convertir de Pulgadas a Centimetros
        b. Convertir de Pulgadas a Metros
        c. Convertir de Pulgadas a Pies
        d. Convertir de Centimetros a Pulgadas
        e. Convertir de Centimetros a Metros
        f. Convertir de Centimetros a Pies

    """
    print(opcion3)
    opcion3=input("Seleccione que opción desea: ")

    if opcion3=="a":
        medida=float(input("Ingrese las Pulgadas: "))
        print(medida * 2.54)
    elif opcion3=="b":
        medida=float(input("Ingrese las Pulgadas: "))
        print(medida * 0.0254)
    elif opcion3=="c":
        medida=float(input("Ingrese las Pulgadas: "))
        print(medida*0.08333333)
    elif opcion3=="d":
        medida=float(input("Ingrese los Centimetros: "))
        print(medida*0.39370079)
    elif opcion3=="e":
        medida=float(input("Ingrese los Centimetros: "))
        print(medida*0.01)
    elif opcion3=="f":
        medida=float(input("Ingrese los Centimetros: "))
        print(medida*0.0328084)
    else:
        print("Error")
    
else:
    print("Número inválido")